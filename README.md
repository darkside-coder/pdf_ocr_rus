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
![Структруа решения](https://user-images.githubusercontent.com/13415975/138608460-c7dfa288-0d2f-45a5-a038-1ecf693ed264.jpg)

### Пример c использованием API
#### Исходный файл [documents_files_197_prikazpr-113-20.pdf](https://github.com/darkside-coder/pdf_ocr_rus/files/7406081/documents_files_197_prikazpr-113-20.pdf) 

#### Пример ответа 
```{
    "message": "File: documents_files_197_prikazpr-113-20.pdf successfully uploaded ",
    "text": "ПРАВИТЕЛЬСТВО <ADDR>  ГОСУДАРСТВЕННАЯ <NAME> ПО КОНТРОЛЮ ЗА <NAME> <NAME> НЕДВИЖИМОСТИ <NAME> <ADDR>  ГОСУДАРСТВЕННОЕ БЮДЖЕТНОЕ УЧРЕЖДЕНИЕ <NAME> <ADDR> «МОСКОВСКИЙ КОНТРОЛЬНО-МОНИТОРИНГОВЫЙ ЦЕНТР НЕДВИЖИМОСТИ»  ПРИКАЗ  <NAME> # <NAME> довоу № /7 773/#22 <DATE> ДР- ЕЙО  «О назначении лиц, уполномоченных на проведение мероприятий <NAME> <NAME> <NAME> фактического <NAME> зданий (строений, <NAME> <NAME> нежилых <NAME> <NAME> целей налогообложения»  В <NAME> <NAME> <NAME> <NAME_REG> <ADDR> <NAME> <DATE> мая <DATE> г. № <DATE> «О <NAME> <NAME> <NAME> фактического <NAME> зданий (строений, <NAME> <NAME> нежилых <NAME> <NAME> целей налогообложения» <NAME>  <DATE> Утвердить <NAME> государственных <NAME> <NAME> Госинспекции <NAME>  недвижимости — (далее — — государственные <NAME> <NAME> работников <NAME_REG>  <NAME> учреждения <NAME>  <ADDR> — «Московский <NAME> <NAME> недвижимости» (далее — ГБУ «МКМЦН»), уполномоченных на проведение мероприятий <NAME> <NAME> <NAME> фактического <NAME> зданий (строений, <NAME> <NAME> нежилых <NAME> <NAME> целей налогообложения (приложение).  <DATE> Руководителям <NAME> <NAME> довести <NAME> <NAME> до <NAME> государственных <NAME> Госинспекции <NAME> недвижимости <NAME> работников ГБУ «МКМЦН», указанных <NAME> приложении <NAME> <NAME> <NAME> роспись <NAME> <NAME> его <NAME>  <DATE> Управлению — <NAME>  <NAME> Госинспекции — <NAME> недвижимости <NAME> размещение <NAME> <NAME> <NAME> <NAME> приложением <NAME> <NAME>  «Результаты — <NAME> мероприятий <NAME> <NAME> фактического — <NAME> раздела — «Документы» на — <NAME> \f2  Госинспекции <NAME> недвижимости на  <NAME> <NAME> <NAME> — <ADDR> Брз:/Лучу\\у то$.ги/ре!.  4. Признать утратившим <NAME> <NAME> Госинспекции <NAME> недвижимости <NAME> <DATE> марта <DATE> г. № ПР-<DATUM>«О назначении лиц, уполномоченных на проведение мероприятий <NAME> <NAME> <NAME> фактического <NAME> зданий (строений, <NAME> <NAME> нежилых <NAME> <NAME> целей налогообложения».  <DATE> <NAME> <NAME> <NAME> <NAME> <NAME> <NAME> <DATE> <NAME> <DATE> г.  <DATE> Контроль за <NAME> <NAME> <NAME> <NAME> на заместителя начальника Госинспекции <NAME> недвижимости <NAME_REG> <ADDR> на <NAME> ГБУ «МКМЦН» <NAME_REG> Д.А.  Начальник Директор  Госинспекции <NAME> недвижимости ДБУ«МКМЦН» <NAME>  <URL> <URL>  <NAME> <NAME>  <DATE> ® <ADDR>                \fПриложение  <NAME> <NAME> <NAME> Госинспекции <NAME> недвижимости <NAME> ГБУ «МКМЦН»  <NAME> « » _ /етвген” <DATE> г.  № /7/- 777 <DATE> / <NAME> <NAME>  Список государственных <NAME> <NAME> Госинспекции <NAME> недвижимости <NAME> работников ГБУ «МКМЦР», уполномоченных на проведение мероприятий <NAME> <NAME> <NAME> фактического <NAME> зданий (строений, <NAME> <NAME> нежилых <NAME> <NAME> целей налогообложения  №№ <NAME> <NAME> <NAME> государственных <NAME> <NAME> Госинспекции <NAME> недвижимости  *  <NAME> <ADDR> <NAME>  *  <NAME_REG> <NAME> <NAME>  <DATE>  9)  ° | <NAME> <NAME> <ADDR>  рьч  ° | Зельчан <NAME> <ADDR> ` | <NAME> <ADDR> <NAME> <NAME_REG> Ринат <NAME_REG>  ° | <NAME> <NAME> <ADDR> <NAME_REG> <NAME> <NAME>  <NAME> <ADDR> <NAME>  — <NAME> <NAME>  <DATE> <NAME> <NAME> <ADDR>  расной аснний  <NAME> <NAME> <ADDR>  <NAME_REG> <NAME> <NAME>  <DATE>  <DATE>  <NAME> <NAME> <NAME>  <NAME_REG> <NAME_REG> <NAME_REG>  — \\Ф )  ° | <NAME_REG> <NAME> <ADDR>  ° | <NAME_REG> <ADDR> <ADDR>  <NAME> <NAME> <ADDR>  ронной. @@)  жа | н — | <  * | <NAME> <ADDR> <ADDR> \f20.  <NAME_REG> <NAME> <ADDR>  <NAME_REG> <NAME> <ADDR>  *  - <DATE>  <NAME> <NAME> <NAME>  <NAME> <ADDR> <NAME>  9)  й <NAME>  <NAME_REG> <ADDR> <ADDR>  ' | <NAME_REG> <NAME> <ADDR>  *  <DATE>  <NAME_REG> <ADDR> <NAME>  <DATE>  <NAME> <NAME> <ADDR>  <NAME>  *  <NAME> <NAME> <NAME>  <NAME>  <NAME> <NAME> <NAME>  <NAME_REG> <NAME> <NAME_REG>  <DATE>  *  <NAME> <NAME> <ADDR>  —  <NAME> <NAME> <NAME>  *  <NAME_REG> <ADDR> <ADDR>  <NAME>  <NAME> <ADDR> <NAME>  <DATE> Чернявский <NAME> <ADDR>  ‘ю | ©Э2| — <NAME> | <NAME> | <NAME> <NAME> <© | © — ^ +  <DATE> <DATE>  <NAME_REG> <NAME> <NAME>  <DATE> <NAME> <NAME> <ADDR>  <DATE> —  <NAME> <NAME> <NAME>  <NAME>  <NAME_REG> <NAME> <NAME_REG>  <ADDR> <NAME> <ADDR>  *  <ADDR> <NAME> <NAME_REG> 4  —  *  <ADDR> <NAME> <NAME>  + <NAME>  <NAME_REG> <NAME> <NAME>  9)  44 <DATE>  +> +> 9  <NAME> <NAME> <ADDR>  <NAME> <NAME> <NAME>  +  \"  <NAME> <NAME> <NAME> \f46. 47.  <NAME_REG> <ADDR> <NAME> <NAME> <NAME> <NAME_REG>  <NAME_REG> <NAME> <NAME>  <NAME> <NAME>  <NAME_REG> Ксения <ADDR>  л <  ' | <ADDR> <ADDR> <NAME> <DATE>  <DATE>  <NAME> <NAME> <ADDR>  Камышанский <ADDR> <NAME>  <DATE>  <DATE>  <NAME> <NAME> <ADDR>  <NAME> <NAME> <ADDR>  <NAME>  *  <DATE>  <NAME> <NAME> <NAME>  <NAME_REG> <ADDR> <NAME>  \\ФД`  <NAME_REG> <NAME> <ADDR>  *  <DATE>  <NAME> <NAME> <NAME> <NAME_REG> <NAME> <NAME> <NAME_REG> <ADDR> <NAME>  *  <NAME> <NAME> <ADDR>  <NAME> <DATE>  <ADDR> <NAME> <NAME>  <DATE>  <ADDR> <ADDR> <ADDR>  <NAME> <ADDR> <NAME_REG>  ©^  <NAME> <ADDR> <NAME>  ©` (Ф» <DATE> \\Ф <NAME> л <DATE>  <NAME_REG> <NAME> <ADDR> ‘ | <NAME_REG> <NAME> <NAME> <NAME> <NAME> <ADDR> <NAME_REG> <NAME> <ADDR>  *  <NAME> <ADDR> <NAME>  — —  72.  <NAME> <NAME> <NAME>  <ADDR> <ADDR> <NAME>  —  *  <NAME> <NAME> <ADDR>  —) ©` \f*  <DATE> 76. 7. 8.  <ADDR> <NAME> <NAME_REG>  —  <NAME_REG> <NAME> <NAME> <NAME> <NAME> <ADDR>  <NAME_REG> <NAME_REG> <NAME>  —  <NAME> <NAME> <NAME>  — —  ' | <NAME> <NAME> <NAME>  <NAME_REG> <NAME> <ADDR> 8  —  <NAME> <NAME> <NAME>  <NAME>  *  <NAME> <ADDR> <ADDR>  <DATE>  <NAME_REG> <ADDR> <ADDR>  +  <NAME_REG> <ADDR> <ADDR>  <NAME> <NAME>  Зоря <NAME> <NAME_REG>  <NAME_REG> Павел <NAME>  ©со —`  *  <NAME_REG> <NAME> <ADDR>  <NAME>  <NAME_REG> <NAME_REG> <NAME_REG> <NAME_REG> <NAME> <NAME>  <NAME> <NAME> <ADDR>  `о  <NAME_REG> <ADDR> <ADDR>  © <NAME>  *  <NAME> <ADDR> <NAME>  <NAME>  *  94.  <NAME> <ADDR> <NAME>  Гогохия Вахтанг <NAME_REG>  © <NAME>  <NAME> <ADDR> <NAME>  <NAME_REG> <ADDR> <NAME>  ©  *  <NAME> <NAME> <NAME> <NAME_REG> <NAME> <NAME>  <ADDR> <ADDR> <NAME_REG> <DATE>  <DATE>  <NAME> <NAME> <NAME>  <NAME> <NAME> —  <NAME> <NAME> <NAME> \f102. <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE>  < л  *  <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE>  <NAME> <NAME> \\Ф  <DATE> <DATE> <DATE> <DATE> <DATE>  <DATE> +  <NAME> <NAME> <ADDR>  <NAME_REG> <NAME> <NAME>  ||  <NAME_REG> <NAME> <NAME>  Лисагор <NAME> <NAME> <NAME_REG> <NAME> <NAME> <NAME> <NAME> <NAME> <NAME_REG> <NAME> <NAME> <NAME_REG> <NAME> <ADDR> <NAME> <ADDR> <NAME> <ADDR> <ADDR> <NAME> <NAME_REG> <ADDR> <NAME_REG> <NAME> <NAME> <ADDR> Скорик <NAME> <NAME> <NAME_REG> <NAME> <ADDR> <NAME> <NAME> <NAME> <NAME_REG> <NAME_REG> <NAME> <NAME_REG> <NAME> <NAME> <NAME> <NAME> <NAME> <NAME_REG> <NAME> <NAME_REG> <NAME_REG> <ADDR> <ADDR> <NAME> <NAME> <NAME> <NAME_REG> <ADDR> <ADDR> <NAME_REG> Владислав <NAME> <NAME> <NAME> <NAME> <ADDR> <NAME> <ADDR> Грушецкий <ADDR> <ADDR> <NAME> <NAME> <NAME>  <NAME_REG> <NAME> <ADDR> \f130. <DATE> <DATE>  <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE>  # #  <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE> <DATE>  <ADDR> <NAME> <NAME> <NAME_REG> <NAME> <ADDR> <NAME> <NAME> <NAME> <NAME_REG> <NAME> <NAME> Контио <NAME> <ADDR> <NAME> <NAME> <ADDR> <NAME_REG> Владислав <ADDR> <NAME_REG> Павел <ADDR> <NAME> <NAME> <NAME> <NAME_REG> <NAME> <ADDR> <NAME> <ADDR> <NAME_REG> <NAME> <NAME> <ADDR> Столярчук Станислав <NAME_REG>  <NAME_REG> <ADDR> <NAME>  <NAME> <NAME> <NAME> работников ГБУ «МКМЦН» <NAME> <ADDR> <NAME> <NAME_REG> <ADDR> <ADDR> Василюк Петр <ADDR> <ADDR> <NAME> <NAME> <NAME_REG> <ADDR> <NAME> <NAME_REG> <NAME> <NAME_REG> <NAME> <NAME> <NAME> <NAME_REG> <NAME_REG> <NAME_REG> <NAME_REG> <NAME> <ADDR> <NAME> <ADDR> <ADDR> <NAME_REG> <ADDR> <ADDR> <NAME_REG> <ADDR> <NAME>  <NAME> <ADDR> <ADDR> \f161.                        ы ”‘0 ч Ч ”^ <DATE> ?, ч <NAME> \\› * ® @ <NAME> аАО <NAME> ее <NAME> ВА <NAME> ‘Ё-›%Ё „ н ч <NAME> ^ й л <NAME> ©; УпРавление <NAME> ® Э5М }® ©Ё <NAME> пЕ ЕВ : РВЕЛЬЕ <NAME> В ЕЕ @ ЗЗ доабоы <NAME> РЕ ЗЕЙ ы <NAME> дФКУМЁНТ&мИ <NAME> › <NAME> ` \"Ё:_;'% <NAME> „М\"\\\\ж“@& ’Э‹‚і <NAME>     \f"
}```
