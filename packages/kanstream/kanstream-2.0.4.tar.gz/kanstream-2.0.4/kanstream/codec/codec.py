from enum import Enum

from .h264 import H264Encoder, H264Decoder
from .h265 import H265Encoder, H265Decoder
from .vp9 import VP9Encoder, VP9Decoder


class CodecType(Enum):
    H264 = 'h264'
    H265 = 'h265'
    VP9 = 'vp9'


class Codec(object):

    @staticmethod
    def create_encoder(codec_type: CodecType | str, **kwargs):
        match codec_type:
            case CodecType.H264 | CodecType.H264.value:
                return H264Encoder(**kwargs)
            
            case CodecType.VP9 | CodecType.VP9.value:
                return VP9Encoder(**kwargs)
            
            case CodecType.H265 | CodecType.H265.value:
                return H265Encoder(**kwargs)
            
            case _:
                raise ValueError(f'Unsupported codec type: {codec_type}')

    @staticmethod
    def create_decoder(codec_type: CodecType, **kwargs):
        match codec_type:
            case CodecType.H264 | CodecType.H264.value:
                return H264Decoder(**kwargs)

            case CodecType.VP9 | CodecType.VP9.value:
                return VP9Decoder(**kwargs)

            case CodecType.H265 | CodecType.H265.value:
                return H265Decoder(**kwargs)

            case _:
                raise ValueError(f'Unsupported codec type: {codec_type}')
