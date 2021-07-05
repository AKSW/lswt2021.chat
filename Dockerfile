FROM python:3.6

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 4 main:app
