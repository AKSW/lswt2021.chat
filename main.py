from flask import Flask
from flask_socketio import SocketIO, emit
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somelswtsecret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('client_message')
def receive_message (client_msg):
    client_msg['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    emit('server_message', client_msg, broadcast=True)

# @socketio.on('connect')
# def test_connect(auth):
#     emit('my response', {'data': 'Connected'})
#
# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
