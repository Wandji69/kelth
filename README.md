# Kelth - System Monitoring and Logging Tool

A comprehensive Python-based system monitoring tool that captures and logs keyboard input, screenshots, screen recordings, and audio in parallel using multi-threading.

## Features

- **Keystroke Logging**: Captures all keyboard input with proper handling of special keys (space, enter, backspace)
- **Screenshot Capture**: Periodically captures screenshots at configurable intervals
- **Screen Recording**: Records the entire screen as MP4 video at 20 FPS
- **Audio Recording**: Records system audio as MP3 format
- **Multi-threaded**: All logging operations run concurrently without blocking each other
- **Organized Output**: All logs are saved to the `logs/` directory with timestamped filenames

## Project Structure

```bash
kelth/
├── main.py                 # Main entry point - starts all logging threads
├── requirement.txt         # Python dependencies
├── logger/
│   ├── __init__.py        # Package initialization
│   ├── keylogger.py       # Keystroke capture module
│   ├── screenshot.py      # Screenshot capture module
│   ├── video.py           # Screen recording module
│   ├── audio.py           # Audio recording module
│   └── utils.py           # Utility functions
└── logs/                  # Output directory for all recordings
    ├── keystrokes.txt     # Logged keystrokes
    ├── screenshot_*.png   # Captured screenshots
    ├── recording_*.mp4    # Screen recordings
    └── audio.mp3          # Audio recording
```

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd kelth
```

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

1. Install dependencies:

```bash
pip install -r requirement.txt
```

## Usage

Run the program:

```bash
python3 main.py
```

The program will:

- Start 4 concurrent threads for keystroke, screenshot, video, and audio logging
- Record for 30 seconds by default
- Save all output to the `logs/` directory
- Press `Ctrl+C` to stop early

## Output Files

- **keystrokes.txt**: Plain text file containing all typed characters and sentences
- **screenshot_*.png**: Sequential PNG screenshots captured every 2 seconds
- **recording_*.mp4**: MP4 video file of the screen recording
- **audio.mp3**: MP3 audio file of system audio

## Requirements

- Python 3.8+
- libpulse (for audio recording)
- X11 display server (for screenshots on Linux)

See `requirement.txt` for full Python package dependencies.

## Configuration

Modify durations and settings in the respective module functions:

- `keylogger.start()` - Runs indefinitely
- `screenshot.capture_screenshot()` - Default 30 seconds
- `video.start_recording()` - Default 30 seconds
- `audio.record_audio()` - Default 30 seconds

## Notes

- The keystroke logger properly handles backspace by removing the last character from the log
- Screenshots are captured periodically to avoid excessive disk usage
- Video is encoded as H.264 MP4 for better compatibility
- Audio is converted from WAV to MP3 for smaller file size
