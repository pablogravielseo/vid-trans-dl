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
    url "https://files.pythonhosted.org/packages/a9/a7/d8fd6c85e5ad93f99ad9ffdea7e7bc6cdc9f9da9bf58e27f38f535d14641/yt_dlp-2025.2.19-py3-none-any.whl"
    sha256 "a1d8a4b6d3e87d3a6b3c3e9a7c8e5c3f1a5b01d3dbd11a5d7b7c2f5d7c166a08"
  end

  resource "openai-whisper" do
    url "https://files.pythonhosted.org/packages/d0/7e/8a9c1f9b0b9c9a0c4c5c1e2c1a5e8a6d2a5d5f0a3c5c4d0a3a8c5c4d0a3a8/openai-whisper-20240930.tar.gz"
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
