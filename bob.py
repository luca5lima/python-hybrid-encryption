from flask import Flask, request
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import pickle

app = Flask(__name__)

# Bob gera suas chaves RSA
chave_privada_bob = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

chave_publica_bob = chave_privada_bob.public_key()
print("Bob gerou suas chaves RSA.")

app.run(
    host="127.0.0.1",
    port=5001
)
