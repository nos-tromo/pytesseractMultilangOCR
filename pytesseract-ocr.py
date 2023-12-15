# CONFIGURE BEFORE USAGE
# configure tesseract executable path
# download tessdata from https://tesseract-ocr.github.io/tessdoc/Data-Files.html and store in tesseract directory
# input data and output directory
# language code
# see the tesseract documentation


import os

import pytesseract
from deep_translator import GoogleTranslator
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'CONFIGURE_TESSERACT_EXECUTABLE_PATH'

class OCR:

    def __init__(self, file, output_path):
        self.file = file
        filename = os.path.basename(self.file)
        self.filename, _ = os.path.splitext(filename)
        self.output_path = output_path

    def apply_ocr(self, lang, config):
        try:
            img = Image.open(self.file)
        except IOError as e:
            print(f"Error opening image: {e}")
            return None
        self.text = pytesseract.image_to_string(img, lang=lang, config=config)
        with open(f'{self.output_path}/{self.filename}.txt', 'w', encoding='utf-8') as f:
            f.write(self.text)
        return self.text

    def translate_ocr(self):
        translation = GoogleTranslator(source='auto', target='english').translate(self.text)
        with open(f'{self.output_path}/{self.filename}_translation.txt', 'w', encoding='utf-8') as f:
            f.write(translation)
        return translation
    
data = 'CONFIGURE_INPUT_DATA'
output_path = 'CONFIGURE_OUTPUT_DIRECTORY'
lang = 'ENTER_ISO_639-2_LANGUAGE_CODE'
config = '--oem 1' '--psm 6' # works fine for the most data, but should be adjusted when encountering errors

ocr = OCR(data, output_path)

text = ocr.apply_ocr(lang, config)
print(text)

translation = ocr.translate_ocr()
print(translation)