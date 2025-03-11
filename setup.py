#!/usr/bin/env python3
"""
Setup script for vid-trans-dl.
"""
from setuptools import setup, find_packages

setup(
    name="vid-trans-dl",
    version="0.1.0",
    description="A command-line tool to download videos and transcribe their audio to text",
    author="Pablo Graviel Seo",
    packages=find_packages(),
    install_requires=[
        "yt-dlp>=2023.0.0",
        "openai-whisper>=20230314",
    ],
    entry_points={
        "console_scripts": [
            "vid-trans-dl=vid_trans_dl.cli:main",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 