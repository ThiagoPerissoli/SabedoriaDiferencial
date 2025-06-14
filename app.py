from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Aplicativo rodando com Flask no Render"
