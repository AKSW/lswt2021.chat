FROM python:3.6

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD gunicorn -b 0.0.0.0:8080 -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 main:app
