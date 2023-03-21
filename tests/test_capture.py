import cv2
import numpy as np
from src.capture import capture_screen


def test_capture_screen():
    screenshot = capture_screen()
    assert isinstance(screenshot, np.ndarray)
    assert screenshot.shape[2] == 3
    assert screenshot.dtype == np.uint8
