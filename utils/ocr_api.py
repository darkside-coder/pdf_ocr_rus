import logging
import pytesseract
import os, sys, shutil
from PIL import Image, ImageEnhance, ImageFilter

import utils.removePD_api as pd_clear
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def jpegToTextAPI(dirpath):
    f = []
    text = ''
    for (dirpath, dirnames, filenames) in os.walk(dirpath):
        f.extend(filenames)
    for file_jpg in f:
        fullname_file_jpg = os.path.join(dirpath, file_jpg)
        print(f'Распознование файла: {fullname_file_jpg}')
        if os.path.exists(fullname_file_jpg):
            im = Image.open(fullname_file_jpg)
            im = im.filter(ImageFilter.MedianFilter())
            enhancer = ImageEnhance.Contrast(im)
            im = enhancer.enhance(2)
            im = im.convert('1')
            temp_jpeg =os.path.join('temp', 'temp.jpg')
            im.save(temp_jpeg)
            text += pytesseract.image_to_string(Image.open(temp_jpeg), lang='rus')

    text = pd_clear.removePersonalData(text)        
    return text