import pyautogui
import cv2
import numpy as np
import os
import time

def capture_screenshot(duration=30, interval=2.0):
    """Capture screenshots periodically for the specified duration"""
    os.makedirs("logs", exist_ok=True)
    start_time = time.time()
    counter = 0
    
    while time.time() - start_time < duration:
        try:
            img = pyautogui.screenshot()
            frame = np.array(img)
            screenshot_path = os.path.join("logs", f"screenshot_{counter:04d}.png")
            cv2.imwrite(screenshot_path, frame)
            counter += 1
            time.sleep(interval)
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
            time.sleep(1)