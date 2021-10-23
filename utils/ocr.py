import logging
import pytesseract
import os, sys, shutil
from PIL import Image, ImageEnhance, ImageFilter
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def jpegToText():
    for (dirpath, dirnames, filenames) in os.walk('jpegs'):
        if len(dirpath) != 0 and len(dirnames) == 0 and len(filenames) != 0:

            # создаем папку, которой будет храниться файл с распознанным текстом
            print((dirpath, dirnames, filenames))
            dirs = dirpath.split(os.sep)
            filename_txt = dirs[-1] + '.txt'
            dirs[0] = 'doc_txts'
            dirpath_txt = os.path.join(*dirs[:-1])
            if os.path.exists(dirpath_txt):
                shutil.rmtree(dirpath_txt, ignore_errors=True)
            os.makedirs(dirpath_txt)

            # распознаем файл
            with open(os.path.join(dirpath_txt, filename_txt), 'a+') as f:
                for file_jpg in filenames:
                    fullname_file_jpg = os.path.join(dirpath, file_jpg)
                    print(fullname_file_jpg)
                    if os.path.exists(fullname_file_jpg):
                        logging.info(f'Распознование: {fullname_file_jpg}')
                        im = Image.open(fullname_file_jpg)
                        im = im.filter(ImageFilter.MedianFilter())
                        enhancer = ImageEnhance.Contrast(im)
                        im = enhancer.enhance(2)
                        im = im.convert('1')
                        temp_jpeg =os.path.join('temp', 'temp.jpg')
                        im.save(temp_jpeg)
                        text = pytesseract.image_to_string(Image.open(temp_jpeg), lang='rus')
                        f.write(text)
                        # text = str(((pytesseract.image_to_string(Image.open(fullname_file_jpg)))))
