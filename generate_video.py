from PIL import Image, ImageDraw, ImageFont
import os
import subprocess
from gtts import gTTS

def process_image(input_image, output_image, text="Sample Text",font_size = 40):
    """Load an image, overlay text, apply transformation, and save it."""
    image = Image.open(input_image)
    draw = ImageDraw.Draw(image)
    # Apply transformation
    color = 255, 255,255
    image = image.convert("L")
    
    image = image.rotate(90)
    
    image = image.resize((image.width // 2, image.height // 2)) 
    font = ImageFont.load_default().font_variant(size=font_size)
    draw = ImageDraw.Draw(image)
    txt = "Hello World"
    draw.text((15, 25), txt, font=font)
    image.save(output_image)

# Step 1: Create narration using gTTS
def create_narration(text, output_file="narration.mp3"):
    """Create an MP3 file from text using Google Text-to-Speech"""
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(output_file)
    return output_file

# Step 2: Mix narration with background music using ffmpeg
import subprocess

import subprocess

def mix_audio(input_files, output_file):
    # Generate the ffmpeg command to mix the audio files
    command = ['ffmpeg']
    
    # Add each input audio file to the command
    for file in input_files:
        command.extend(['-i', file])
    
    # Set the mix filter for all input files and trim the result to 5 seconds
    command.extend(['-filter_complex', f'amix=inputs={len(input_files)}:duration=longest', '-ac', '2', '-t', '5', output_file])

    # Run the ffmpeg command
    subprocess.run(command)

if __name__ == "__main__":
    # Example usage:
    input_files = ['audio1.mp3', 'audio2.mp3', 'audio3.mp3']  # Replace with your file paths
    output_file = 'mixed_output_5_seconds.mp3'  # Output file name
    
    mix_audio(input_files, output_file)
    print(f"Audio files mixed and saved as {output_file}")



    print(f"Mixed audio saved to {output_file}")
def create_video(image_file, narration_file, music_file, output_video="output.mp4", duration=5, captions="Sample Caption"):
    """Generate a short video using FFmpeg with background music and captions."""
    
    caption_file = "captions.srt"
    
    
    
    with open(caption_file, "w") as f:
        f.write("1\n")
        f.write("00:00:00,000 --> 00:00:05,000\n")
        f.write(f"{captions}\n")
    
    
    ffmpeg_cmd = [
    "ffmpeg", "-y",
    "-loop", "1", "-i", image_file,
    "-c:v", "libx264", "-t", str(duration), "-pix_fmt", "yuv420p",
    "-vf", "subtitles=captions.srt:force_style='FontSize=24,PrimaryColour=&HFFFFFF'",
    "-an",  
    "-shortest", output_video
]
    
    subprocess.run(ffmpeg_cmd, check=True)
def add_audio_to_video(video_path, audio_path, output_path):
    
    if not os.path.isfile(video_path):
        print(f"Error: Video file not found: {video_path}")
        return False
        
    if not os.path.isfile(audio_path):
        print(f"Error: Audio file not found: {audio_path}")
        return False
    
    # Build ffmpeg command
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",           
        "-c:a", "aac",           
        "-b:a", "192k",           
        "-shortest",              
        "-map", "0:v:0",          
        "-map", "1:a:0",          
        output_path
    ]
    
    # Run the command
    print("Running ffmpeg command:")
    print(" ".join(cmd))
    
    
    result = subprocess.run(cmd, capture_output=True, text=True)
        
def main():
    input_image = input("input image: ") 
    imagetext = input("image text: ") 
    output_image = input("output path: ")
    music_file = input("music file: ")  
    narration_file = input("input image: ")
    output_video = input("output video_path: ")
    caption_text = input("caption text: ")
    final_vid = "final_"+output_video
    
    process_image(input_image, output_image, text=imagetext)
    create_video(output_image, narration_file, music_file, output_video, duration=5, captions=caption_text)
    mix_audio(['narration.mp3','aria.mp3'],'mixed_audio.mp3')
    add_audio_to_video('final_video.mp4','mixed_audio.mp3',final_vid)
    

if __name__ == "__main__":
    main()
