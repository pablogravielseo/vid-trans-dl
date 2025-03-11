# vid-trans-dl

A command-line tool to download videos and transcribe their audio to text using AssemblyAI.

## Features

- Download videos from various platforms (YouTube, Vimeo, etc.) using yt-dlp
- Extract audio from videos
- Transcribe audio to text using AssemblyAI (cloud-based, fast and accurate)
- Automatic language detection (for audio with at least 50 seconds of speech)
- Support for multiple languages
- Customizable output location
- Option to keep the downloaded audio file

## Requirements

- Python 3.7 or higher
- ffmpeg
- yt-dlp
- AssemblyAI API key (sign up at https://www.assemblyai.com/)

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
# Basic usage (requires ASSEMBLYAI_API_KEY environment variable or .env.local file)
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID"

# Specify output file
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -o transcript.txt

# Specify language (e.g., Portuguese)
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -l pt

# Keep the downloaded audio file
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -k

# Provide AssemblyAI API key directly
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" --assemblyai-key "YOUR_API_KEY"
```

### Available Options

- `-o, --output`: Output file path for the transcription (default: transcript.txt)
- `-l, --language`: Language code for transcription (e.g., 'pt' for Portuguese, 'en' for English). If not specified, automatic language detection will be used by default.
- `-k, --keep-audio`: Keep the downloaded audio file after transcription
- `-d, --max-duration`: Maximum duration in seconds to transcribe
- `--assemblyai-key`: AssemblyAI API key

## Usage Examples

### Transcribe a YouTube video with automatic language detection

```bash
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -o transcript.txt
```

### Transcribe a YouTube video in Portuguese

```bash
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -l pt -o transcript.txt
```

### Download a video, transcribe it, and keep the audio file

```bash
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -k
```

### Transcribe only the first 5 minutes of a video

```bash
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -d 300
```

### Using AssemblyAI with .env.local file

You can store your AssemblyAI API key in a `.env.local` file:

1. Create a `.env.local` file in your working directory
2. Add your API key: `ASSEMBLYAI_API_KEY=your_api_key_here`
3. Run the command without specifying the key:

```bash
vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID"
```

## How It Works

1. The tool uses yt-dlp to download the video and extract the audio
2. The audio is temporarily saved in MP3 format
3. The audio is transcribed using AssemblyAI's cloud-based service
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

### Error: "AssemblyAI API key is required"

You need to provide your AssemblyAI API key. You can:
1. Pass it directly with `--assemblyai-key "YOUR_API_KEY"`
2. Set it as an environment variable: `export ASSEMBLYAI_API_KEY="YOUR_API_KEY"`
3. Create a `.env.local` file with `ASSEMBLYAI_API_KEY=your_api_key_here`

## License

MIT