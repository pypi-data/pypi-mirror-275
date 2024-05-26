import os
from argparse import ArgumentParser

def main(): 
  parser = ArgumentParser()
  parser.add_argument('--images', type=str, help='KV connection string to images')
  parser.add_argument('--db', required=True, type=str, help='DB URL')

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)


  args = parser.parse_args()
  db = args.db

  from dslog import Logger, formatters
  logger = Logger.stderr().format(formatters.click)

  logger(f'Running API...')
  logger(f'- DB URL: "{db.split(":")[0]}://[...]{db.split(":")[1][-16:]}"')
  logger(f'- Images URL: {args.images.split(":")[0]}://[...]{args.images.split(":")[1][-16:]}')

  from kv.api import KV, LocatableKV
  from sqlalchemy import create_engine
  from moveread.dfy import run_api

  images = KV[bytes].of(args.images)
  images_path = getattr(images, 'base_path', None)
  if not isinstance(images, LocatableKV):
    raise ValueError('Images KV must be locatable')

  engine = create_engine(db)
  run_api(images, engine, images_path=images_path, port=args.port, host=args.host, logger=logger)

if __name__ == '__main__':
  import os
  import sys
  from dotenv import load_dotenv
  load_dotenv()

  MOCK = True
  if MOCK:
    os.chdir('/home/m4rs/mr-github/modes/moveread-dfy/infra/local-db')
    SQL_CONN_STR = 'sqlite:///db.sqlite'
    IMAGES = 'file:///home/m4rs/mr-github/modes/moveread-dfy/local-db/images'
    sys.argv.extend(f'--images {IMAGES} --db {SQL_CONN_STR}'.split(' '))
  else:
    SQL_CONN_STR = os.environ['SQL_CONN_STR']
    BLOB_CONN_STR = os.environ['BLOB_CONN_STR']
    sys.argv.extend(f'--images {BLOB_CONN_STR} --db {SQL_CONN_STR}'.split(' '))
  
  main()