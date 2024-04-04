from flask import Flask
from time import gmtime, strftime
import requests

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    bitcoin_price = data['bitcoin']['usd']
    return bitcoin_price

@app.route("/")
def defaultfunc():
    return "Hello, try using /btc in the URL."

@app.route("/btc")
def hello_world():
    return "Price of BTC @ " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " : " + str(get_btc_price())

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000)
