#### Пререквизиты: 

* Запуск в OS Windows.

#### Установка:
* Установить пакеты из *requirements.txt*: ```py -m pip install -r requirements.txt ```
* Скачать и установить [Tesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
* По [инструкции](https://ocrmypdf.readthedocs.io/en/latest/languages.html) добавить библиотеку для распознования русского языка. 
- Скачиваем [файл](https://github.com/tesseract-ocr/tessdata/blob/main/rus.traineddata)
- Подкладываем сюда ```C:\\Program Files\\Tesseract-OCR\\tessdata```

#### Использование:
##### Батчовый анализ документов
1) Добавить в doc_samples файлы для распознования
2) Выполнить ```py run.py```
3) В директории *doc_txts* появится текстовое представление распознанных документов

##### Демо API для загрузки документов:
1) запустить ```py app.py```
2) локально поднимется flask-сервер с возможностью отправки POST-запросов содержащих файл для распознования (пока работает только с PDF)
3) результат запроса текст из файла с удаленными персональными данными
###### Пример запроса
![postman_hack](https://user-images.githubusercontent.com/13415975/138608133-54d01142-2220-4f9e-9fdd-ee6f2549aaee.png)

#### Структура решения
![Структруа решения](https://user-images.githubusercontent.com/13415975/138608352-268b36fe-0989-4b01-a0cd-0eee2fda5750.jpg)
