"""H.265编解码模块"""

import av
import av.video

from .h264 import H264Encoder, H264Decoder
from ..utils.calculate_bitrate import calculate_bitrate


class H265Decoder(H264Decoder):

    def __init__(self):
        super().__init__()
        self._container = av.open(self._raw_data, format="h265", mode='r')


class H265Encoder(H264Encoder):

    def set_config(self, height: int, width: int, fps: int, gop_size=60, bit_rate=0):
        container: av.OutputContainer = av.open('output.h265', 'w')
        stream: av.video.stream.VideoStream = container.add_stream('h265', rate=30)

        # 编码器相关配置
        bit_rate = bit_rate if bit_rate > 0 else calculate_bitrate(width, height, fps)
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
