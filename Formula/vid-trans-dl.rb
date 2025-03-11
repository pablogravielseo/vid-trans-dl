class VidTransDl < Formula
  include Language::Python::Virtualenv

  desc "Command-line tool to download videos and transcribe their audio to text"
  homepage "https://github.com/pablogravielseo/vid-trans-dl"
  url "https://github.com/pablogravielseo/vid-trans-dl/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "a8d7dab43002b34acc647dcae335bff067831b97e09b49b846a708e04c39777f"
  license "MIT"

  depends_on "ffmpeg"
  depends_on "python@3.9"

  resource "yt-dlp" do
    url "https://files.pythonhosted.org/packages/53/36/ef300ba4a228b74612d4013b43ed303a0d6d2de17a71fc37e0b821577e0a/yt_dlp-2025.2.19.tar.gz"
    sha256 "f33ca76df2e4db31880f2fe408d44f5058d9f135015b13e50610dfbe78245bea"
  end

  resource "openai-whisper" do
    url "https://files.pythonhosted.org/packages/f5/77/952ca71515f81919bd8a6a4a3f89a27b09e73880cebf90957eda8f2f8545/openai-whisper-20240930.tar.gz"
    sha256 "b7178e9c1615576807a300024f4daa6353f7e1a815dac5e38c33f1ef055dd2d2"
  end

  # Add other dependencies as needed

  def install
    virtualenv_install_with_resources
  end

  test do
    system bin/"vid-trans-dl", "--help"
  end
end
