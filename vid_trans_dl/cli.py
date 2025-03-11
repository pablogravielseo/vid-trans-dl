#!/usr/bin/env python3
"""
vid-trans-dl CLI - Download videos and transcribe their audio to text.
"""
import os
import sys
import argparse
import tempfile
import subprocess
from pathlib import Path


def check_dependencies():
    """Check if required dependencies are installed."""
    dependencies = ["yt-dlp", "ffmpeg"]
    missing = []
    
    for dep in dependencies:
        try:
            subprocess.run(
                ["which", dep], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                check=True
            )
        except subprocess.CalledProcessError:
            missing.append(dep)
    
    if missing:
        print(f"Error: Missing dependencies: {', '.join(missing)}")
        print("Please install them before continuing.")
        if "yt-dlp" in missing:
            print("Install yt-dlp: pip install yt-dlp")
        if "ffmpeg" in missing:
            print("Install ffmpeg: brew install ffmpeg (macOS) or apt install ffmpeg (Ubuntu/Debian)")
        sys.exit(1)


def download_audio(url, output_path, audio_format="mp3"):
    """Download audio from a video URL using yt-dlp."""
    print(f"Downloading audio from: {url}")
    
    cmd = [
        "yt-dlp",
        "-x",  # Extract audio
        f"--audio-format={audio_format}",
        "-o", output_path,
        url
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"Audio downloaded successfully to: {output_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error downloading audio: {e}")
        return False


def transcribe_audio(audio_path, language=None, model="small"):
    """Transcribe audio file using Whisper."""
    print(f"Transcribing audio file: {audio_path}")
    
    cmd = ["whisper", audio_path, f"--model={model}"]
    
    if language:
        cmd.append(f"--language={language}")
    
    try:
        subprocess.run(cmd, check=True)
        # Whisper creates a .txt file with the same name as the audio file
        transcript_path = Path(audio_path).with_suffix('.txt')
        if transcript_path.exists():
            print(f"Transcription completed: {transcript_path}")
            return transcript_path
        else:
            print("Transcription completed but output file not found.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error transcribing audio: {e}")
        return None


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Download videos and transcribe their audio to text."
    )
    parser.add_argument(
        "url", 
        help="URL of the video to download and transcribe"
    )
    parser.add_argument(
        "-o", "--output", 
        help="Output file path for the transcription (default: transcript.txt)",
        default="transcript.txt"
    )
    parser.add_argument(
        "-l", "--language", 
        help="Language code for transcription (e.g., 'pt' for Portuguese, 'en' for English)",
        default=None
    )
    parser.add_argument(
        "-m", "--model", 
        help="Whisper model size (tiny, base, small, medium, large)",
        default="small"
    )
    parser.add_argument(
        "-k", "--keep-audio", 
        help="Keep the downloaded audio file after transcription",
        action="store_true"
    )
    
    args = parser.parse_args()
    
    # Check if dependencies are installed
    check_dependencies()
    
    # Create a temporary directory for the audio file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Set the audio file path
        audio_path = os.path.join(temp_dir, "audio.mp3")
        
        # Download the audio
        if not download_audio(args.url, audio_path):
            sys.exit(1)
        
        # Transcribe the audio
        transcript_path = transcribe_audio(audio_path, args.language, args.model)
        
        if transcript_path:
            # Copy the transcript to the desired output location
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(transcript_path, 'r') as src, open(output_path, 'w') as dst:
                dst.write(src.read())
            
            print(f"Transcript saved to: {output_path}")
            
            # If keep_audio is True, copy the audio file to the current directory
            if args.keep_audio:
                audio_output = Path(f"audio_{Path(audio_path).stem}.mp3")
                with open(audio_path, 'rb') as src, open(audio_output, 'wb') as dst:
                    dst.write(src.read())
                print(f"Audio saved to: {audio_output}")
        else:
            print("Transcription failed.")
            sys.exit(1)


if __name__ == "__main__":
    main() 