from utils import transform
from utils import ocr

if __name__ == '__main__':
    transform.fileToJpeg()
    ocr.jpegToText()