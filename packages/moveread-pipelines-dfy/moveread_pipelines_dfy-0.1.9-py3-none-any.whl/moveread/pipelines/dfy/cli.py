from argparse import ArgumentParser
from math import e

def main():
  parser = ArgumentParser()
  parser.add_argument('-b', '--base-path', required=True)
  parser.add_argument('--images', required=True)

  parser.add_argument('-p', '--port', default=8000, type=int)
  parser.add_argument('--host', default='0.0.0.0', type=str)

  args = parser.parse_args()

  import os
  from dslog import Logger
  base_path = os.path.join(os.getcwd(), args.base_path)
  images_path = os.path.join(os.getcwd(), args.images)
  
  logger = Logger.click().prefix('[DFY]')
  logger(f'Running preprocessing...')
  logger(f'Images path: "{images_path}"')
  logger(f'Internal path: "{base_path}"')
  
  from typing import Sequence, Mapping
  import asyncio
  from multiprocessing import Process
  import uvicorn
  from kv.fs import FilesystemKV
  from kv.sqlite import SQLiteKV
  from q.kv import QueueKV
  import moveread.pipelines.preprocess as pre
  from moveread.pipelines.game_preprocess import Game
  from moveread.pipelines.dfy import Workflow, Result

  images = FilesystemKV[bytes](images_path)

  db_path = os.path.join(base_path, 'data.sqlite')
  def make_queue(path: Sequence[str], type: type):
    return QueueKV.sqlite(type, db_path, table='-'.join(['queues', *path]))

  Qout = make_queue(['output'], Result)
  queues = Workflow.make_queues(make_queue, Qout)
  artifacts = Workflow.artifacts(**queues['internal'])(
    images=images, images_path=images_path,
    games=SQLiteKV.validated(Game, db_path, 'games'),
    imgGameIds=SQLiteKV.at(db_path, 'game-ids'),
    received_imgs=SQLiteKV.validated(Mapping[str, pre.Result], db_path, 'received-im')
  )

  ps = {
    id: Process(target=asyncio.run, args=(f,)) for id, f in artifacts.processes.items()
  } | {
    'api': Process(target=uvicorn.run, args=(artifacts.api,), kwargs={'host': args.host, 'port': args.port})
  }
  for id, p in ps.items():
    p.start()
    logger(f'Process "{id}" started at PID {p.pid}')
  for p in ps.values():
    p.join()

if __name__ == '__main__':
  import sys
  import os
  path = '/home/m4rs/mr-github/rnd/data/moveread-pipelines/backend/4.dfy/demo'
  os.makedirs(path, exist_ok=True)
  os.chdir(path)
  sys.argv.extend('-b internal/ --images images'.split(' '))
  main()