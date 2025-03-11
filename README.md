# vid-trans-dl

A command-line tool to download videos and transcribe their audio to text.

## Features

- Download videos from various platforms (YouTube, Vimeo, etc.) using yt-dlp
- Extract audio from videos
- Transcribe audio to text using OpenAI's Whisper
- Support for multiple languages
- Customizable output location
- Option to keep the downloaded audio file

## Requirements

- Python 3.7 or higher
- ffmpeg
- yt-dlp
- OpenAI Whisper

## Installation

### Using Homebrew (macOS)

The easiest way to install on macOS is using Homebrew:

```bash
brew tap pablogravielseo/tools
brew install vid-trans-dl
```

### Install Dependencies

First, make sure you have ffmpeg installed:

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg

# Windows (using Chocolatey)
choco install ffmpeg
```

### Install vid-trans-dl Manually

```bash
# Clone the repository
git clone https://github.com/pablogravielseo/vid-trans-dl.git
cd vid-trans-dl

# Install the package globally
./install.sh
```

The installation script will check for required dependencies and install the package globally on your system.

## Usage

```bash
# Basic usage
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID"

# Specify output file
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -o transcript.txt

# Specify language (e.g., Portuguese)
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -l pt

# Use a different Whisper model
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -m medium

# Keep the downloaded audio file
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -k
```

### Available Options

- `-o, --output`: Output file path for the transcription (default: transcript.txt)
- `-l, --language`: Language code for transcription (e.g., 'pt' for Portuguese, 'en' for English)
- `-m, --model`: Whisper model size (tiny, base, small, medium, large)
- `-k, --keep-audio`: Keep the downloaded audio file after transcription

## Usage Examples

### Transcribe a YouTube video in Portuguese

```bash
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -l pt -o transcript.txt
```

### Transcribe a video with higher accuracy

```bash
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -m large
```

### Download a video, transcribe it, and keep the audio file

```bash
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -k
```

## How It Works

1. The tool uses yt-dlp to download the video and extract the audio
2. The audio is temporarily saved in MP3 format
3. OpenAI's Whisper is used to transcribe the audio to text
4. The transcription is saved to the specified output file
5. The temporary audio file is deleted (unless the -k option is used)

## Uninstallation

### Uninstall via Homebrew

If you installed using Homebrew:

```bash
brew uninstall vid-trans-dl
```

### Uninstall Manual Installation

If you installed manually, run:

```bash
./uninstall.sh
```

## Troubleshooting

### Error: "ffmpeg not found"

Make sure you have ffmpeg installed on your system:

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg
```

### Error: "yt-dlp not found"

yt-dlp should be installed automatically during installation, but you can install it manually:

```bash
pip install yt-dlp
```

### Error: "Whisper not found"

Whisper should be installed automatically during installation, but you can install it manually:

```bash
pip install openai-whisper
```

## License

MIT