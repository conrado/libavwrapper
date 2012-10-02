LibAVWrapper
============

LibAVWrapper is a small wrapper for the avconv encoder. You can append
Codec, Filters and other parameterStores to the AVConv class and then run the
resulting command.

>>> from libavwrapper import AVConv, Input, Output, VideoCodec, VideoFilter
>>> videofilter = VideoFilter().crop(300, 200)
>>> codec = VideoCodec('webm')
>>> input_video = Input('old')
>>> output_video = Output('new', videofilter, codec)
>>> AVConv('avconv', input_video, output_video)
<AVConv ['avconv', '-i', 'old', '-vf', 'crop=300:200', '-vcodec', 'webm', 'new']>
