#criar ambiente virtual (.venv)
#pip install flask
#pip install python-socketio
#pip install flask-socketio
#pip install simple-websocket
#importar flask
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*") #permitir qualquer origem de enviar mensagens ao ecessar o site

#criar a funcionalidade de enviar mensagens

@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast = True)

#Criar a primeira página (primeira rota)

@app.route("/") #Decorator
def homepage():
    return render_template("index.html")
#rodar o aplicativo
socketio.run(app, host="localhost") # define que o app vai rodar no seu servidor local, ou seja, na internet em que o seu computador tá conectado