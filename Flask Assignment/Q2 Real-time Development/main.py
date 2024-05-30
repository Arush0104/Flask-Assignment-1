from flask import Flask, render_template
import eventlet
import requests
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

def get_stock_price():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    headers = {
        "X-CoinAPI-Key": "EB668C7C-F39C-42E0-8C2A-3B2B5DBDF049"  # Replace with your actual CoinAPI key
    }
    response = requests.get(url, headers=headers)
    return response.json()['rate']

@app.route("/")
def index():
    STOCK_SYMBOL = "BTC/USD"  # Define the stock symbol
    return render_template("index.html", STOCK_SYMBOL=STOCK_SYMBOL)

@socketio.on('connect')
def handle_connect():
    live_price = get_stock_price()
    socketio.emit('live_price', live_price)
    socketio.start_background_task(background_task)

def background_task():
    while True:
        live_price = get_stock_price()
        socketio.emit('live_price', live_price)
        eventlet.sleep(10)

if __name__ == '__main__':
    socketio.run(app)
    app.run()
