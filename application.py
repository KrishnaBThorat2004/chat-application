from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Store messages in memory (for demonstration purposes)
messages = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    messages.append(data)
    emit('receive_message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
