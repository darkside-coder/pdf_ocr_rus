import os, sys, shutil
from pdf2image import convert_from_path
from PIL import Image
import logging
 

def fileToJpeg():
    # получаем список всех доступных для распознования файлов
    files = [] 
    for (dirpath, dirnames, filenames) in os.walk('doc_samples'):
        for name in filenames:
            filename, file_extension = os.path.splitext(name)
            files.append((os.path.join(dirpath, name), dirpath, name, file_extension))

    # приводим всей файлы к формату jpeg и сохраняем в директорию jpegs
    for file, dirpath, filename, file_extension in files:
        if os.path.isfile(file):
            if file_extension == '.pdf':
                filename_without_extension, file_extension = os.path.splitext(filename)
                dir_for_jpegs = os.path.join('jpegs' + '\\' + dirpath, filename_without_extension)
                if os.path.exists(dir_for_jpegs):
                    shutil.rmtree(dir_for_jpegs, ignore_errors=True)
                os.makedirs(dir_for_jpegs)
            
                pages = convert_from_path(file, 500, poppler_path='poppler-0.68.0\\bin')
                for page_number, page in enumerate(pages):
                    file_jpg = os.path.join(dir_for_jpegs, str(page_number) + '.jpg')
                    logging.info(f'Создание {file_jpg}')
                    page.save(file_jpg, 'JPEG')