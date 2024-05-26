from typing import Unpack
import asyncio
from datetime import timedelta
from sqlalchemy import Engine
from dslog import Logger
from kv.api import KV
from q.api import ReadQueue
from scoresheet_models import ModelID
from moveread.core import CoreAPI
import moveread.pipelines.dfy as dfy
from ._puller import puller
from ._pusher import pusher

def artifacts(*, Qout: ReadQueue[dfy.Result], **queues: Unpack[dfy.Workflow.Queues]):
  
  def _bound(
      logger = Logger.click().prefix('[DFY]'), *,
      engine: Engine, output_core: CoreAPI,
      online_images: KV[bytes], polling_interval = timedelta(seconds=30),
      **params: Unpack[dfy.Params]
    ) -> dfy.Artifacts:
    
    async def coro():
      await asyncio.gather(
        puller(
          queues['Qin'], engine, polling_interval=polling_interval,
          logger=logger.prefix('[PULLER]'),
          online_images=online_images, local_images=params['images']
        ),
        pusher(Qout, engine, output_core=output_core, images=params['images'], logger=logger.prefix('[PUSHER]'))
      )

    artifs = dfy.Workflow.artifacts(**queues['internal'])(logger=logger, **params)
    artifs.processes = { 'connect': coro() } | {
      f'doer-{id}': proc for id, proc in artifs.processes.items()
    }
    
    return artifs
  
  return _bound