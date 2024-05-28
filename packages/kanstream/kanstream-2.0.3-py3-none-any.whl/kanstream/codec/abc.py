from abc import ABC, abstractmethod


class VideoEncodeABC(ABC):

    @abstractmethod
    def encode(self, *args):
        """对np.ndarray进行编码"""

    @abstractmethod
    def close(self):
        """退出编码"""


class VideoDecodeABC(ABC):

    @abstractmethod
    def decode(self, *args):
        """对bytes进行解码"""

    @abstractmethod
    def close(self):
        """退出解码"""