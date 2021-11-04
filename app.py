import pytesseract

from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

a = Image.open('시.jpg')
result = pytesseract.image_to_string(a,lang='kor')
print(result)