class VidTransDl < Formula
  include Language::Python::Virtualenv

  desc "Command-line tool to download videos and transcribe their audio to text with automatic language detection"
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

  resource "python-dotenv" do
    url "https://files.pythonhosted.org/packages/31/06/1ef763af20d0572c032fa22882cfbfb005fba6e7300715a37840858c919e/python-dotenv-1.0.0.tar.gz"
    sha256 "a8df96034aae6d2d50a4ebe8216326c61c3eb64836776504fcca410e5937a3ba"
  end

  resource "assemblyai" do
    url "https://files.pythonhosted.org/packages/b5/f7/6f9a0c0d9d2f6d0f8d8d3bd4f3c6c9a9b5c1e8a3a4c5a04f3d3d3e2a8cb3/assemblyai-0.37.0.tar.gz"
    sha256 "4f1e57e906564baf50424a7779bbcd0b8d838c90cceb19f70ce47f294a1700f6"
  end

  def install
    virtualenv_install_with_resources
  end

  def caveats
    <<~EOS
      To use vid-trans-dl, you need an AssemblyAI API key.
      You can sign up for a free API key at https://www.assemblyai.com/

      Once you have your API key, you can set it in one of the following ways:
      1. Create a .env.local file in your current directory with:
         ASSEMBLYAI_API_KEY=your_api_key
      2. Set the ASSEMBLYAI_API_KEY environment variable:
         export ASSEMBLYAI_API_KEY=your_api_key
      3. Provide it directly when running the command:
         vid-trans-dl --assemblyai-key your_api_key "https://www.youtube.com/watch?v=VIDEO_ID"

      By default, vid-trans-dl will automatically detect the language of the audio.
      For reliable language detection, the audio must contain at least 50 seconds of speech.
      You can also specify a language with the -l option (e.g., -l pt for Portuguese).
    EOS
  end

  test do
    # Test that the command exists and can show help
    assert_match "Download videos and transcribe their audio to text", shell_output("#{bin}/vid-trans-dl --help")
  end
end
