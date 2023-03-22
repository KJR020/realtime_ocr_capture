import time
from capture import capture_screen
from ocr import perform_ocr

if __name__ == "__main__":
    while True:
        # Capture the screen
        screenshot = capture_screen()

        # Perform OCR on the screenshot
        text = perform_ocr(screenshot)

        # Print the recognized text
        print("Recognized text:", text)

        # Wait for a while before capturing the screen again
        time.sleep(5)
