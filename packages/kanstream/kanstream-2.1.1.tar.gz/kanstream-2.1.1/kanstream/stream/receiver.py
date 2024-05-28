from asyncio.streams import StreamWriter, StreamReader

import numpy as np
from loguru import logger

from .protobuf import *
from .base import NettyClient
from .frame_pb2 import MessageBody
from ..codec import Codec, CodecType


class StreamReceiver(NettyClient):
    """
    这个类用于从服务器接收视频流。

    它使用NettyClient来与服务器建立连接并接收视频流。

    Attributes:
        host: 服务器的IP地址。
        port: 服务器的端口号。
        client_id: 接收器的客户端ID。
        codec_type: 视频流的编解码类型。

    Methods:
        connect: 创建一个新的StreamReceiver实例的类方法。
        receive: 从服务端获取一个解码后的视频帧。
    """

    def __init__(self, host: str, port: int, client_id: str, codec_type: CodecType = CodecType.H264):
        super().__init__(host, port, client_id)
        self._decoder = Codec.create_decoder(codec_type)
        self.start()

    async def _send(self, writer: StreamWriter):

        hmb = MessageBody(
            client_id=self.client_id,
            message_type=2
        )
        message = hmb.SerializeToString()
        message = ProtobufVarint32LengthFieldEncoder.encode(message)

        writer.write(message)
        await writer.drain()

        logger.info(f'【stream-receiver】发送响应成功,响应信息:{hmb},pullchannel:{self.client_id}')

    async def _receive(self, reader: StreamReader):
        fail_i = 0
        decoder = ProtobufVarint32FrameDecoder()

        while self.status:
            data = await reader.read(1024)
            decoded_messages = decoder.decode(data)

            if len(decoded_messages) != 1:
                continue

            hmb = MessageBody()
            byte_data = decoded_messages[0]
            hmb.parse(byte_data)

            if hmb.message_type == 3:
                break

            frame_bytes = hmb.image_buffer
            for frame in self._decoder.decode(frame_bytes):
                if frame is None:
                    fail_i += 1
                    logger.warning(f'【stream-receiver】解码失败{fail_i}次,client_id:{self.client_id}')
                    continue
                self.queue.put(frame)

    def receive(self) -> np.ndarray:
        """
        从服务端获取一个解码后的视频帧。

        Returns:
            解码后的视频帧。
        """
        return self.queue.get()
