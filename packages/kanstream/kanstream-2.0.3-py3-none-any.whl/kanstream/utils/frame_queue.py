from queue import Queue
from typing import Any

from loguru import logger


class FrameQueue(object):

    def __init__(self, max_size=10, name: str = None):
        self._queue = Queue(max_size)
        self.name = name

    def put(self, item: Any):
        if self._queue.full():
            self._queue.get()
            logger.warning(f"Frame queue {self.name} is full, dropping oldest frame")
        self._queue.put(item)

    def get(self) -> Any:
        return self._queue.get()
