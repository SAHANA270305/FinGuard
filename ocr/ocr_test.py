import cv2
import pytesseract

# For Windows, set Tesseract path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread("sample_statement.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)
print("Extracted text:")
print(text)

