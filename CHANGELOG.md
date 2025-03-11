# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-03-11

### Added

- Initial functionality to download videos using yt-dlp
- Functionality to transcribe audio using OpenAI Whisper
- Support for different languages in transcription
- Option to keep the audio file after transcription
- Support for different Whisper models (tiny, base, small, medium, large)
- Installation and uninstallation scripts
- Homebrew formula for easy installation on macOS systems
- Detailed documentation in README.md
- Guide for publishing on Homebrew (HOMEBREW_GUIDE.md)

### Fixed

- Nothing to report, this is the initial version

### Changed

- Nothing to report, this is the initial version

### Removed

- Nothing to report, this is the initial version

## [Unreleased]

### Added

- Automatic language detection feature when no language is specified
- Updated to use AssemblyAI API version 0.37.0
- Improved documentation about language detection in README and Homebrew formula

### Fixed

- Fixed language parameter handling in AssemblyAI transcription

### Changed

- Made automatic language detection the default behavior when no language is specified
- Updated help text to clarify language detection functionality

### Planned for future versions

- Support for downloading playlists
- Optional graphical interface
- Option to export transcriptions in different formats (SRT, VTT, etc.)
- Support for automatic translation of transcriptions 