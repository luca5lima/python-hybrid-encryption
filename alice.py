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

    # --- PARTE V ---
    # 1. Gera uma chave AES e cifra a mensagem
    chave_aes = AESGCM.generate_key(bit_length=256)
    mensagem_bytes = mensagem.encode()
    aes = AESGCM(chave_aes)
    nonce = os.urandom(12)
    mensagem_cifrada = aes.encrypt(nonce, mensagem_bytes, None)

    # 2. Protege a chave secreta AES com a chave pública de Bob (RSA)
    chave_aes_cifrada = chave_publica_bob.encrypt(
        chave_aes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # 3. Cria o pacote com todos os dados cifrados
    pacote = {
        "nonce": nonce,
        "mensagem_cifrada": mensagem_cifrada,
        "chave_aes_cifrada": chave_aes_cifrada
    }

    # 4. Serializa e envia para o Bob
    dados = pickle.dumps(pacote)
    resposta = requests.post(f"{URL_BOB}/message", data=dados)
    print("Bob respondeu:", resposta.text)

    return "Mensagem recebida por Alice!"

app.run(
    host="127.0.0.1",
    port=5002
)