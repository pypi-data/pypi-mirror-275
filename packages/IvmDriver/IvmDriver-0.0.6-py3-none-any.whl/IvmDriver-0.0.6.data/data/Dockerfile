FROM python:3.7
COPY . /driver
WORKDIR /driver
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt 
# RUN python main.py
# EXPOSE $PORT
# # CMD waitress-serve --listen=127.0.0.1:$PORT app:app
# CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
CMD python mainDriver.py
