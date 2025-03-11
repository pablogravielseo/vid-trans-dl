#!/bin/bash
# Installation script for vid-trans-dl

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "pip3 is not installed. Please install pip3 and try again."
    exit 1
fi

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null; then
    echo "ffmpeg is not installed."
    
    # Check the OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        echo "Installing ffmpeg using Homebrew..."
        if ! command -v brew &> /dev/null; then
            echo "Homebrew is not installed. Please install Homebrew first:"
            echo '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
            exit 1
        fi
        brew install ffmpeg
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        echo "Please install ffmpeg using your package manager:"
        echo "For Ubuntu/Debian: sudo apt install ffmpeg"
        echo "For Fedora: sudo dnf install ffmpeg"
        echo "For Arch Linux: sudo pacman -S ffmpeg"
        exit 1
    else
        echo "Unsupported OS. Please install ffmpeg manually."
        exit 1
    fi
fi

# Install the package
echo "Installing vid-trans-dl..."
pip3 install -e .

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "Installation successful!"
    echo "You can now use the vid-trans-dl command from anywhere."
    echo "Example usage: vid-trans-dl \"https://www.youtube.com/watch?v=VIDEO_ID\""
else
    echo "Installation failed. Please check the error messages above."
    exit 1
fi 