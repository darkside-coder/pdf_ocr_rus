#### Установка:
* Установить пакеты из *requirements.txt*: ```py -m pip install -r requirements.txt ```
* Скачать и установить [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
* По [инструкции](https://ocrmypdf.readthedocs.io/en/latest/languages.html) добавить библиотеку для распознования русского языка

#### Использование:
1) Добавить в doc_samples файлы для распознования
2) Выполнить ```py run.py```
3) В директории *doc_txts* появится текстовое представление распознанных документов
