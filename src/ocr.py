import cv2
import tesseract


def perform_ocr(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR using tesseract
    text = tesseract.image_to_string(gray_image)
    return text
