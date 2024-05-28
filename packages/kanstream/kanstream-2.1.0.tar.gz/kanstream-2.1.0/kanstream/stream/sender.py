from asyncio.streams import StreamWriter

import numpy as np

from .base import NettyClient
from .frame_pb2 import MessageBody
from .protobuf import *
from ..codec import Codec, CodecType


class StreamSender(NettyClient):
    """
    这个类用于向服务器发送视频流。

    它使用NettyClient来与服务器建立连接并发送视频流。

    Attributes:
        host: 服务器的IP地址。
        port: 服务器的端口号。
        client_id: 接收器的客户端ID。
        codec_type: 视频流的编码类型。

    Methods:
        connect: 创建一个新的StreamSender实例的类方法。
        send: 向服务器发送视频流。
    """

    def __init__(self, host: str, port: int, client_id: str, codec_type=CodecType.H264):
        super().__init__(host, port, client_id)
        self._encoder = Codec.create_encoder(codec_type)
        self._size = (0, 0)
        self.start()

    async def _send(self, writer: StreamWriter):

        while self.status:
            frame: np.ndarray = self.queue.get()

            height, width = frame.shape[:2]
            if self._size != (size := (height, width)):
                self._size = size
                self._encoder.set_config(height, width, 30)

            for frame_bytes, is_keyframe in self._encoder.encode(frame):
                hmb = MessageBody(
                    client_id=self.client_id,
                    message_type=1,
                    width=width,
                    height=height,
                    image_buffer=frame_bytes,
                    codec_type=2,
                    length=len(frame_bytes),
                    frames_per_second=30,
                    render_time_ms=0,
                    frame_type=3 if is_keyframe else 4
                )
                message = hmb.SerializeToString()
                message = ProtobufVarint32LengthFieldEncoder.encode(message)
                writer.write(message)
                await writer.drain()

    def send(self, frame: np.ndarray):
        """
        向服务器发送视频帧。
        Args:
            frame(np.ndarray): 视频帧。
        """

        self.queue.put(frame)
