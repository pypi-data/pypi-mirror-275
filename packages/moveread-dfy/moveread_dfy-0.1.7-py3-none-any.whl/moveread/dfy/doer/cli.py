from argparse import ArgumentParser
import os

def env(variable: str) -> dict:
  if (value := os.getenv(variable)) is not None:
    return dict(default=value)
  return dict(required=True)

def main():
  parser = ArgumentParser()
  parser.add_argument('--dfy-db', **env('DFY_DB'), help='Database URL')
  parser.add_argument('--dfy-images', type=str, help='KV conn str to DFY images')
  parser.add_argument('--doer-db', **env('DOER_DB'), help='Internal database URL, for queues and stuff')
  parser.add_argument('--doer-images', **env('DOER_IMAGES'), type=str, help='KV conn str to doer images')
  parser.add_argument('--core-games', **env('CORE_GAMES'), type=str, help='KV conn str to output Core games')
  parser.add_argument('--core-blobs', **env('CORE_BLOBS'), type=str, help='KV conn str to output Core blobs')

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)

  args = parser.parse_args()

  from dslog import Logger
  dfy_db = args.dfy_db
  doer_db = args.doer_db
  dfy_images = args.dfy_images
  doer_images = args.doer_images
  core_games = args.core_games
  core_blobs = args.core_blobs
  
  logger = Logger.click().prefix('[DFY]')
  logger(f'Running...')
  logger(f'- Database URL: "{dfy_db}"')
  logger(f'- Internal DB URL: "{doer_db}"')
  logger(f'- Doer images URL: "{doer_images}"')
  logger(f'- DFY images URL: "{dfy_images}"')
  logger(f'- Core games URL: "{core_games}"')
  logger(f'- Core blobs URL: "{core_blobs}"')

  from typing import Sequence
  from functools import cache
  import asyncio
  from multiprocessing import Process
  import uvicorn
  from sqlmodel import create_engine
  from kv.api import KV
  from kv.fs import FilesystemKV
  from kv.sql import SQLKV
  from q.kv import QueueKV
  from moveread.core import CoreAPI
  import moveread.pipelines.preprocess as pre
  from moveread.pipelines.game_preprocess import Game
  from moveread.pipelines.dfy import Workflow, Result
  from moveread.dfy.doer.main import artifacts
  
  online_engine = create_engine(dfy_db)
  engine = create_engine(doer_db)

  @cache
  def make_queue(path: Sequence[str], type: type):
    kv = SQLKV(type, engine, table='-'.join(['queues', *path]))
    return QueueKV(kv)
  
  Qout = make_queue(('output',), Result)
  queues = Workflow.make_queues(make_queue, Qout)

  online_images = KV.of(dfy_images)
  local_images = KV.of(doer_images)
  if isinstance(local_images, FilesystemKV):
    images_path = local_images.base_path
  else:
    images_path = None

  core = CoreAPI.of(core_games, core_blobs)
  
  artifs = artifacts(Qout=Qout, **queues)(
    online_images=online_images,
    images=local_images, images_path=images_path,
    games=SQLKV(Game, engine, 'games'),
    imgGameIds=SQLKV(str, engine, 'game-ids'),
    received_imgs=SQLKV(dict[str, pre.Result], engine, 'received-imgs'),
    engine=online_engine, output_core=core,
  )

  ps = {
    id: Process(target=asyncio.run, args=(f,)) for id, f in artifs.processes.items()
  } | {
    'api': Process(target=uvicorn.run, args=(artifs.api,), kwargs={'host': args.host, 'port': args.port})
  }
  for id, p in ps.items():
    p.start()
    logger(f'Process "{id}" started at PID {p.pid}')
  for p in ps.values():
    p.join()

if __name__ == '__main__':
  import sys
  import os
  from dotenv import load_dotenv
  load_dotenv()

  def params(mock: bool = True):
    if mock:
      path = '/home/m4rs/mr-github/modes/moveread-dfy/infra/doer/local'
      os.makedirs(path, exist_ok=True)
      os.chdir(path)
      os.makedirs('core', exist_ok=True)
      return {
        'dfy-db': 'sqlite:///../../local-db/db.sqlite',
        'dfy-images': 'file://../../local-db/images',
        'doer-images': 'file://images',
        'doer-db': 'sqlite:///db.sqlite',
        'core-games': 'sql+sqlite:///core/games.sqlite;table=games',
        'core-blobs': 'file://core/images',
      }
    else:
      return {
        'dfy-db': os.getenv('DFY_DB'),
        'dfy-images': os.getenv('DFY_IMAGES'),
        'doer-images': os.getenv('DOER_IMAGES'),
        'doer-db': os.getenv('DOER_DB'),
        'core-games': os.getenv('CORE_GAMES'),
        'core-blobs': os.getenv('CORE_BLOBS'),
      }

  args = []
  for k, v in params().items():
    args.append(f'--{k}')
    args.append(v)
  print(args)
  sys.argv.extend(args)
  main()