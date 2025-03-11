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

  resource "ffmpeg-python" do
    url "https://files.pythonhosted.org/packages/dd/5e/d5f9105d59c1325759d838af4e973952742fc8a2b62b1c0fb3e5fbdf821a/ffmpeg_python-0.2.0.tar.gz"
    sha256 "65225db34627c578ef0e11c8b1eb528bb35e024752f6f10b78c011f6f64c4127"
  end

  resource "future" do
    url "https://files.pythonhosted.org/packages/a7/b2/5a7c8e2bb15a02569a7ae3e9097a2dd8a3d5d68e07aebd8a3f8a0f6b5b4c/future-1.0.0.tar.gz"
    sha256 "bd2968309307861edae1458a4f8a893fac80aa5924b39c9c64452c5e6851b0b3"
  end

  resource "tqdm" do
    url "https://files.pythonhosted.org/packages/62/06/d5604a70d160f6a6ca5fd2ba25597c24abd5c5ca5f437263d177ac242308/tqdm-4.66.1.tar.gz"
    sha256 "d88e651f9db8d8551a62556d3cff9e3034274ca5d66e93197cf2490e2dcb69c7"
  end

  def install
    virtualenv_install_with_resources
  end

  def caveats
    <<~EOS
      This tool uses OpenAI Whisper for transcription.

      The first time you run it, it will download the selected model.
      Use the --model flag to choose a model:
        - tiny: Fastest, least accurate (default)
        - base: Fast, basic accuracy
        - small: Good balance of speed and accuracy
        - medium: More accurate but slower
        - large: Most accurate, slowest

      For long videos, you can limit the duration with --max-duration:
        vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" --max-duration 300

      Example usage:
        vid-trans-dl "https://www.youtube.com/watch?v=VIDEO_ID" -o transcript.txt
    EOS
  end

  test do
    system bin/"vid-trans-dl", "--help"
  end
end
