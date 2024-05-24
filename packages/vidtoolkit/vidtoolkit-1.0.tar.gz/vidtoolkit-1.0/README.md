# vidtoolkit

vidtoolkit is a comprehensive toolkit for video processing, including subtitles, watermarks, trimming, thumbnails, and MP4 to HLS conversion.

## Installation

```bash
pip install vidtoolkit
```

## Usage

### Adding Subtitles

```python
from vidtoolkit.video_subtitle import VideoSubtitle

video = VideoSubtitle('input_video.mp4')
video.add_subtitle('Hello, World!', 0, 5, position=(10, 10), fontsize=24, color='white')
```

### Adding Subtitles from SRT

```python
from vidtoolkit.video_subtitle import VideoSubtitle

video = VideoSubtitle('input_video.mp4')
video.add_subtitle_from_srt('subtitles.srt')
```

### Adding Text Watermark

```python
from vidtoolkit.video_watermarking import VideoWatermarking

video = VideoWatermarking('input_video.mp4')
video.add_text_watermark('Sample Watermark', position=('center', 'bottom'), fontsize=24, color='white')
```

### Adding Image Watermark

```python
from vidtoolkit.video_watermarking import VideoWatermarking

video = VideoWatermarking('input_video.mp4')
video.add_image_watermark('watermark.png', position=('right', 'bottom'))
```

### Trimming Video

```python
from vidtoolkit.video_trimming import VideoTrimming

video = VideoTrimming('input_video.mp4')
video.extract_frames(10, 50, with_audio=True)
```

### Generating Thumbnail

```python
from vidtoolkit.video_thumbnailer import VideoThumbnailer

video = VideoThumbnailer('input_video.mp4')
video.generate_thumbnail(100, save_path='thumbnail.jpg')
```

### Converting MP4 to HLS

```python
from vidtoolkit.mp4_to_hls_converter import MP4toHLSConverter

converter = MP4toHLSConverter('input_video.mp4', resolutions=['1920x1080', '1280x720'])
converter.convert()
```


## License

This project is licensed under the LGPL License - see the LICENSE file for details.