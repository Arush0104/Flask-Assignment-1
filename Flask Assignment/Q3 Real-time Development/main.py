from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@app.route('/send_notification', methods=['POST'])
def send_notification():
    message = request.form['message']
    socketio.emit('notification', message)
    return 'Notification sent'

if __name__ == '__main__':
    socketio.run(app)
    app.run(debug=True)