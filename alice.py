from flask import Flask, request

import requests
import pickle

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os

app = Flask(__name__)

URL_BOB = "http://127.0.0.1:5001"

# Alice solicita a chave pública de Bob
resposta = requests.get(
    f"{URL_BOB}/public-key"
)

chave_publica_bob = serialization.load_der_public_key(
    resposta.content
)
print("Alice recebeu a chave pública de Bob.")

@app.route("/send", methods=["POST"])
def enviar_mensagem():
    dados = request.get_json()

    mensagem = dados["mensagem"]

    print("\nAlice recebeu a mensagem:")
    print(mensagem)

    return "Mensagem recebida por Alice!"

app.run(
    host="127.0.0.1",
    port=5002
)
