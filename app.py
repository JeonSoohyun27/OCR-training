
import pytesseract

from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

a = Image.open('ocr-test-image1.png')
result = pytesseract.image_to_string(a)
print(result)
