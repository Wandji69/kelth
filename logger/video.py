import pyautogui
import datetime
import os
import time

# For video recording, use opencv's VideoWriter
import cv2
import numpy as np

class VideoLogger:
    def __init__(self, output_dir='logs/videos', fps=20.0):
        self.output_dir = output_dir
        self.fps = fps
        self.recording = False
        self.video_writer = None
        self.frame_size = None

        # Create the output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def start_recording(self):
        if self.recording:
            print("Already recording.")
            return
        
        # Get the screen size
        screen_width, screen_height = pyautogui.size()
        self.frame_size = (screen_width, screen_height)

        # Create a unique filename based on the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        video_filename = f"{self.output_dir}/recording_{timestamp}.mp4"

        # Initialize the VideoWriter with H.264 codec for MP4
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.video_writer = cv2.VideoWriter(video_filename, fourcc, self.fps, self.frame_size)

        self.recording = True
        print(f"Started recording: {video_filename}")

    def stop_recording(self):
        if not self.recording:
            print("Not currently recording.")
            return
        
        self.recording = False
        self.video_writer.release()
        print("Stopped recording.")

    def log_frame(self):
        if not self.recording:
            return
        
        # Capture the current screen
        screenshot = pyautogui.screenshot()
        
        # Convert the screenshot to a format suitable for OpenCV
        frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        
        # Write the frame to the video file
        self.video_writer.write(frame)


def start_recording(duration=30, output_dir='logs/videos', fps=20.0):
    vl = VideoLogger(output_dir=output_dir, fps=fps)
    vl.start_recording()

    total_frames = int(duration * fps)
    for _ in range(total_frames):
        vl.log_frame()
        time.sleep(1.0 / fps)

    vl.stop_recording()