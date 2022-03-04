from flask import Flask
app = Flask(__name__)

@app.route("/samos123")
def hello():
    return "https://hackerone.com/samos123"
