from datetime import timedelta
import asyncio
from uuid import uuid4
from sqlalchemy import Engine
from sqlalchemy.exc import DatabaseError
from sqlmodel import select, Session
from haskellian import Left, either as E
from dslog import Logger
from kv.api import KV
from q.api import WriteQueue
from chess_pairings import gameId
from moveread.pipelines.dfy import Input
from ..types import Game, Pairing, Tournament, SheetModel

def randomId(tournId: str, group: str, round: str, board: str) -> str:
  return f'{tournId}/{group}/{round}/{board}_{uuid4()}'

def pairing_display(pairing: Pairing):
  pair = pairing.root
  if pair.tag == 'unpaired':
    return 'Unpaired!?'
  
  s = f'{pair.white} - {pair.black}'
  if pair.result is not None:
    s += f' {pair.result}'
  return s


def title(pairing: Pairing, tournId: str, group: str, round: str, board: str) -> str:
  return f'{tournId} {group}/{round}/{board} {pairing_display(pairing)}'

async def puller(
  Qin: WriteQueue[Input], engine: Engine, *,
  online_images: KV[bytes], local_images: KV[bytes],
  polling_interval: timedelta = timedelta(seconds=30),
  logger = Logger.rich().prefix('[PULLER]')
):
  @E.do()
  async def pull_once():
    try:
      with Session(engine) as ses:
        on = Game.tournId == SheetModel.tournId
        stmt = select(Game, SheetModel).join(SheetModel, on).where(Game.status == Game.Status.uploaded)
        for game, model in ses.exec(stmt):
          gid = gameId(game.tournId, game.group, game.round, game.board)
          id = randomId(**gid)
          urls = [img.url for img in game.imgs]
          task = Input(gameId=gid, model=model.model, imgs=urls, title=title(game.pairing, **gid))
          tasks = [online_images.copy(url, local_images, url).run() for url in urls]
          results = await asyncio.gather(*tasks)
          E.sequence(results).unsafe()

          logger(f'Inputting new task for "{id}":', task)
          (await Qin.push(id, task)).unsafe()
          game.status = Game.Status.doing
          ses.add(game)
        ses.commit()


    except DatabaseError as e:
      Left(e).unsafe()


  while True:
    logger('Polling', level='DEBUG')
    r = await pull_once()
    logger('Polled', level='DEBUG')
    if r.tag == 'left':
      logger('Error while pulling', r.value, level='ERROR')
    
    await asyncio.sleep(polling_interval.total_seconds())
