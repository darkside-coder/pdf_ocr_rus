from utils import transform
from utils import ocr
import logging


if __name__ == '__main__':
    logging.info("Поиск файлов для распознования и перевод их в формат .jpeg")
    transform.fileToJpeg()
    logging.info("Распознование файлов...")
    ocr.jpegToText()