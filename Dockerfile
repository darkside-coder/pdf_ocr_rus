FROM jitesoft/tesseract-ocr
RUN train-lang rus --fast
COPY rus.traineddata /usr/share/tessdata
COPY . /app
CMD python3 run.py