import asyncio
from asyncio.streams import StreamWriter, StreamReader
from threading import Thread

from loguru import logger

from ..utils.frame_queue import FrameQueue


class NettyClient(Thread):

    def __init__(self, host: str, port: int, client_id: str):
        super().__init__()
        self.host = host
        self.port = port
        self.client_id = client_id
        self.loop = asyncio.new_event_loop()
        self.queue = FrameQueue(name=client_id)
        self.status = True

    @property
    def is_connected(self):
        return self.status

    @property
    def host_port(self):
        return f'{self.host}:{self.port}'

    @property
    def client_id(self):
        return self._client_id

    async def _send(self, writer: StreamWriter):
        ...

    async def _receive(self, reader: StreamReader):
        ...

    async def _connect(self):
        try:
            reader, writer = await asyncio.open_connection(self.host, self.port)
            task_send = self.loop.create_task(self._send(writer))
            task_receive = self.loop.create_task(self._receive(reader))
            await asyncio.gather(task_send, task_receive)
            writer.close()

        except ConnectionRefusedError as e:
            logger.error(f'【netty】client_id:{self.client_id},异常信息:{str(e)}')

        except Exception:
            logger.exception(f'【netty】client_id:{self.client_id},其他错误')

    def _boot_up(self):
        self.loop.run_until_complete(self._connect())
        self.loop.close()
        logger.info(f'【netty】client_id:{self.client_id},连接关闭')

    def run(self):
        self._boot_up()

    def disconnect(self):
        self.status = False
        self.queue.put(None)
