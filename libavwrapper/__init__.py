# -*- coding: utf8 -*-
"""
    libavwrapper
    ~~~~~~~~~~~~~~~~~~~~

    Simple wrapper for the avconv command.

    :copyright: (c) 2012 by Mathias Koehler, Conrado Buhrer
    :license: BSD, see LICENSE for more details.
"""

__title__ = "libavwrapper"
__author__ = "Mathias Koehler, Conrado Buhrer"
__version__ = "0.1-dev"


from .avconv import AVConv, Input, Output
from .codec import VideoCodec, AudioCodec, NO_AUDIO, NO_VIDEO
from .filter import VideoFilter, AudioFilter
