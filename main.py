import requests
from flask import Flask, render_template
import time

app = Flask(__name__)

def get_price(devise = "EUR"):
    res = requests.get("https://blockchain.info/ticker?base=BTC").json()
    return res[devise]

def get_devises():
    res = requests.get("https://blockchain.info/ticker?base=BTC").json()
    return res

@app.route("/")
def index():
    return render_template("index.html", datas = get_price(), time = time.strftime("%H:%M:%S"), plus = "Par défault : EUR", devises = get_devises())

@app.route("/<dev>")
def single_devise(dev):
    try:
        datas = get_price(dev)
        return render_template("index.html", datas = datas, time = time.strftime("%H:%M:%S"), plus = f"Devise séléctionnée : {dev}",devises = get_devises())
    except:
        res = {"last":"Aucune devise"}
        return render_template("index.html", datas = res, time = "Error")

if __name__ == "__main__":
    app.run(debug=True)