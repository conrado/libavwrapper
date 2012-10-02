#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
LibAVWrapper
~~~~~~~~~~~~~

LibAVWrapper is a small wrapper for the ffmpeg encoder. You can append
Codec, Filters and other ParameterStores to the AVConv class and then run the
resulting command.

>>> from libavwrapper import AVConv , Input, Output, VideoCodec, VideoFilter
>>> codec = VideoCodec('webm')
>>> input_video = Input('old')
>>> output_video = Output('new', videofilter, codec)
>>> AVConv('avconv', input_video, output_video)
<AVConv ['avconv', '-i', 'old', '-vcodec', 'webm', 'new']>


"""

from setuptools import setup

setup(
    name="libavwrapper",
    version="0.1-dev",
    packages=['libavwrapper'],
    author="Conrado Buhrer",
    author_email="conrado@buhrer.net",
    url="http://github.com/conrado/libavwrapper",
    description='A simple wrapper for avconv-cli',
    keywords='Video Convert avconv',
    long_description=__doc__,
    license="BSD",
    test_suite='test',
    tests_require='mock>=0.7.2',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Video',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
