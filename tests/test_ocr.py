import cv2
from src.ocr import perform_ocr


def test_perform_ocr():
    sample_img = cv2.imread("tests/sample_text_image.png", cv2.IMREAD_COLOR)
    result = perform_ocr(sample_img)
    assert isinstance(result, str)
    assert "すみません" in result.lower()
