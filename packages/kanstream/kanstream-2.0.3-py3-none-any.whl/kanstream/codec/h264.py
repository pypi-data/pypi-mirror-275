"""H.264编解码模块"""

import io
from typing import Iterator

import av
import av.video
import numpy as np

from .abc import VideoDecodeABC, VideoEncodeABC
from ..utils.calculate_bitrate import calculate_bitrate


class H264Decoder(VideoDecodeABC):

    def __init__(self):
        super().__init__()
        self._raw_data = io.BytesIO()
        self._cur_pos = 0
        self._container = av.open(self._raw_data, format="h264", mode='r')

    def decode(self, frame_bytes: bytes) -> Iterator[np.ndarray | None]:

        self._raw_data.write(frame_bytes)
        self._raw_data.seek(self._cur_pos)
        for packet in self._container.demux():

            # 过滤音频、字幕
            if packet.stream.type != 'video':
                continue

            if packet.size == 0:
                continue

            self._cur_pos += packet.size

            try:
                frames: Iterator[av.VideoFrame | av.VideoFrame] = packet.decode()
                for frame in frames:

                    # 进一步过滤音频
                    if isinstance(frame, av.AudioFrame):
                        continue

                    img_array = frame.to_ndarray(format='bgr24')

                    yield img_array
            except:
                yield None

    def close(self):
        if self._container is not None:
            self._container.close()
        self._raw_data.close()


class H264Encoder(VideoEncodeABC):

    def __init__(self) -> None:
        super().__init__()
        self._save_video = None
        self._stream = None
        self._container = None

    def set_config(self, height: int, width: int, fps: int, gop_size=60, bit_rate=0):
        container: av.OutputContainer = av.open('output.h264', 'w')
        stream: av.video.stream.VideoStream = container.add_stream('h264', rate=30)

        # 编码器相关配置
        bit_rate = bit_rate if bit_rate > 0 else calculate_bitrate(width, height, fps) * 2
        codec_context = stream.codec_context
        codec_context.bit_rate = bit_rate * 1000
        codec_context.bit_rate_tolerance = 200 * 1000
        codec_context.framerate = fps
        codec_context.gop_size = gop_size
        codec_context.pix_fmt = 'yuv420p'
        codec_context.options = {
            'preset': 'ultrafast',
        }
        stream.height = height
        stream.width = width

        self._stream = stream
        self._container = container

        return bit_rate

    def encode(self, img_array: np.ndarray, to_idr=False) -> Iterator[tuple[bytes, bool]]:
        """将np.ndarray类型的图像编码成字节

        Parameters
        ----------
        img_array : np.ndarray
            图像
        to_idr : bool
            是否将此图像编码为IDR

        """

        frame: av.video.frame.VideoFrame = av.VideoFrame.from_ndarray(img_array, format='bgr24')

        if to_idr is True:
            frame.pict_type = 'I'  # 从此帧开始编码为IDR

        packets = self._stream.encode(frame)  # 编码,即 VideoFrame -> packet

        for packet in packets:
            frame_bytes = bytes(packet)
            yield frame_bytes, packet.is_keyframe

    def close(self):
        if self._container is not None:
            self._container.close()
