from flask import Flask

app = Flask(__name__)

@app.route("/")
def boas_vindas():
  return "Sejam bem-vindos ao Spotify-Clone"

@app.route("/musicas")
def musicas():
  return "Aqui vai ficar as musicas"