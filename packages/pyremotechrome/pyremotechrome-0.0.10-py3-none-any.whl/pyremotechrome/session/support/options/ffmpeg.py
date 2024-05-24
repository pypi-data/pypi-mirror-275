from typing import Union
from dataclasses import dataclass
from pyremotechrome.util import Numbers


@dataclass
class FFMpeg:
    
    ffmpeg_exec: str
    probesize: Union[str, Numbers]
    segment_time: Numbers
    frame_per_second: Numbers
    queue_size_multiplier: Numbers
    audio_itsoffset: Numbers
    maxrate: Union[str, Numbers]
    bufsize: Union[str, Numbers]
    constant_rate_factor: Numbers
