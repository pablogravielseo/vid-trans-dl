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

# Import dotenv for loading environment variables from .env.local file
try:
    from dotenv import load_dotenv
    # Try to load from .env.local first, then fall back to .env if it exists
    env_loaded = load_dotenv('.env.local')
    if not env_loaded:
        load_dotenv('.env')
except ImportError:
    # dotenv is not installed, continue without it
    pass


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


def transcribe_with_assemblyai(audio_path, api_key, max_duration=None):
    """Transcribe audio file using AssemblyAI API."""
    print(f"Transcribing audio file with AssemblyAI: {audio_path}")
    
    try:
        import assemblyai as aai
        
        # Check audio duration if ffmpeg is available and max_duration is specified
        if max_duration:
            try:
                result = subprocess.run(
                    ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", audio_path],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True
                )
                duration = float(result.stdout.strip())
                print(f"Audio duration: {int(duration // 60)} minutes and {int(duration % 60)} seconds")
                
                if duration > max_duration:
                    print(f"Limiting transcription to first {max_duration} seconds of audio")
                    # Trim the audio file
                    import tempfile
                    temp_audio = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
                    subprocess.run(
                        ["ffmpeg", "-i", audio_path, "-t", str(max_duration), "-c:a", "copy", temp_audio],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        check=True
                    )
                    audio_path = temp_audio
            except Exception as e:
                print(f"Warning: Could not determine audio duration or trim audio: {e}")
        
        # Configure API key
        aai.settings.api_key = api_key
        
        # Create a transcriber
        transcriber = aai.Transcriber()
        
        print("Uploading audio to AssemblyAI (this may take a few moments)...")
        transcript = transcriber.transcribe(audio_path)
        
        if transcript.status == "completed":
            print("Transcription completed successfully!")
            
            # Save the transcription to a file
            transcript_path = Path(audio_path).with_suffix('.txt')
            with open(transcript_path, 'w', encoding='utf-8') as f:
                f.write(transcript.text)
            
            print(f"Transcription saved to: {transcript_path}")
            return transcript_path
        else:
            print(f"Transcription failed with status: {transcript.status}")
            if transcript.error:
                print(f"Error: {transcript.error}")
            return None
    except ImportError:
        print("Error: AssemblyAI package not installed. Install with: pip install assemblyai")
        return None
    except Exception as e:
        print(f"Error transcribing audio with AssemblyAI: {e}")
        return None


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="Download videos and transcribe their audio to text using AssemblyAI."
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
        "-k", "--keep-audio", 
        help="Keep the downloaded audio file after transcription",
        action="store_true"
    )
    parser.add_argument(
        "-d", "--max-duration", 
        help="Maximum duration in seconds to transcribe (default: transcribe entire audio)",
        type=int,
        default=None
    )
    parser.add_argument(
        "--assemblyai-key", 
        help="AssemblyAI API key (can also be set via ASSEMBLYAI_API_KEY environment variable or .env.local file)",
        default=None
    )
    
    args = parser.parse_args()
    
    # Check if API key is provided
    api_key = args.assemblyai_key
    if not api_key:
        # Try to get API key from environment variable
        api_key = os.environ.get("ASSEMBLYAI_API_KEY")
        if not api_key:
            print("Error: AssemblyAI API key is required")
            print("You can provide it with --assemblyai-key or set the ASSEMBLYAI_API_KEY environment variable")
            print("You can also create a .env.local file with ASSEMBLYAI_API_KEY=your_key")
            sys.exit(1)
    
    print("Using AssemblyAI for transcription (cloud-based service)")
    
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
        transcript_path = transcribe_with_assemblyai(audio_path, api_key, args.max_duration)
        
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
            print("Transcription failed or was cancelled.")
            sys.exit(1)


if __name__ == "__main__":
    main() 