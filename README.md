# Video Generator

A Python script to generate short videos with text overlays, captions, and mixed audio narration.

## Overview

This tool allows you to:
- Process an image with text overlay and transformations
- Create narration from text using Google Text-to-Speech
- Mix narration with background music
- Generate a video with captions
- Combine the video and mixed audio into a final video

## Installation

### Prerequisites
- FFmpeg (must be installed and available in your PATH)
- PILLOW
- GTTS (Google Text to Speach)


#### On Windows:
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the files to a location on your system
3. Add the FFmpeg bin folder to your system PATH

## Usage

Run the script using:

```bash
python generate_video.py
```

The script will prompt you for the following inputs:
1. `input image`: Path to the source image file
2. `image text`: Text to overlay on the image
3. `output path`: Where to save the processed image
4. `music file`: Path to background music file (MP3)
5. `input image`: Path to narration file (or leave blank to generate from text)
6. `output video_path`: Name for the output video file
7. `caption text`: Text to display as captions in the video

## Example

```
input image: sample.jpg
image text: Hello World
output path: processed_image.jpg
music file: background.mp3
input image: narration.mp3
output video_path: my_video.mp4
caption text: This is a sample video
```

The final video will be saved as `final_my_video.mp4`.

