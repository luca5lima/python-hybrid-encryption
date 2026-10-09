# Python Hybrid Encryption

A practical study of hybrid cryptography using Python, RSA, AES-GCM, and HTTP communication between two applications: Alice and Bob.

## About the Project

This project demonstrates the fundamentals of **hybrid cryptography** through a client-server messaging scenario. Alice sends a message to Bob, using asymmetric cryptography to protect a symmetric encryption key and symmetric cryptography to encrypt the message itself.

The project is based on an academic activity for the Information Security and Auditing course and is intended for educational purposes.

## Objectives

- Understand the differences between symmetric and asymmetric cryptography.
- Generate and exchange RSA public keys.
- Encrypt messages using AES-GCM.
- Protect AES keys using RSA with OAEP padding.
- Build HTTP endpoints with Flask.
- Understand how encrypted data is transmitted and decrypted.
- Practice Python virtual environments and dependency management.

## Technologies

| Technology   | Purpose                                       |
| ------------ | --------------------------------------------- |
| Python       | Main programming language                     |
| RSA          | Asymmetric encryption and key protection      |
| AES-256-GCM  | Message encryption and integrity verification |
| OAEP         | Padding scheme for RSA encryption             |
| Flask        | HTTP API endpoints                            |
| Requests     | HTTP communication between Alice and Bob      |
| Cryptography | Cryptographic primitives and operations       |

## How It Works

The project uses a hybrid encryption workflow:

1. **Bob generates RSA keys.** A public key and a private key are created.
2. **Bob publishes his public key.** Alice retrieves it through the `/public-key` endpoint.
3. **Alice receives a message.** The `/send` endpoint accepts the message through an HTTP POST request.
4. **Alice generates an AES key.** A fresh 256-bit key is generated to encrypt the message using AES-GCM.
5. **Alice protects the AES key.** The AES key is encrypted with Bob's public RSA key using OAEP with SHA-256.
6. **Alice sends the encrypted package.** The package contains the nonce, encrypted message, and encrypted AES key.
7. **Bob decrypts the package.** His private RSA key recovers the AES key, which is then used to decrypt and authenticate the message.

## Architecture

```text
                 1. Request public key
          Alice --------------------------> Bob
                 <--------------------------
                    RSA public key

                 2. Send encrypted package
          Alice --------------------------> Bob
                    HTTP POST /message

                 3. Recover original message
          AES key protected by RSA
          Message encrypted with AES-GCM
```

## Project Structure

```text
python-hybrid-encryption/
├── alice.py          # Message sender and AES encryption
├── bob.py            # RSA key generation and message receiver
├── requirements.txt  # Python dependencies
├── .gitignore        # Files excluded from Git
└── README.md         # Project documentation
```

## Requirements

- Python 3
- pip
- Git (optional, for version control)
- Visual Studio Code or another Python editor

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-hybrid-encryption.git
cd python-hybrid-encryption
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

**Windows PowerShell**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If `requirements.txt` has not been created yet, install the dependencies directly:

```bash
python -m pip install flask cryptography requests
```

### 4. Run Bob

Open the first terminal and execute:

```bash
python bob.py
```

Bob starts the Flask server at `http://127.0.0.1:5001`.

### 5. Run Alice

Open a second terminal, activate the virtual environment, and execute:

```bash
python alice.py
```

Alice starts the Flask server at `http://127.0.0.1:5002`.

Keep both servers running while testing the application.

## API Endpoints

| Endpoint      | Method | Purpose                               |
| ------------- | ------ | ------------------------------------- |
| `/public-key` | GET    | Returns Bob's public RSA key          |
| `/send`       | POST   | Receives a message at Alice           |
| `/message`    | POST   | Receives the encrypted package at Bob |

The `/send` and `/message` endpoints are part of the intended messaging workflow; their complete integration depends on the implementation being finished.

## Security Considerations

This project is for learning and experimentation, not production deployment.

- **AES-GCM** provides message confidentiality and integrity verification.
- **RSA-OAEP** protects the AES encryption key.
- The RSA private key must remain secret.
- The nonce must be unique for each encryption performed with the same AES key; it does not need to be secret.
- The application uses local HTTP communication and does not implement TLS.
- The public key is not authenticated, so the current design does not prevent public-key substitution or man-in-the-middle attacks.
- Python's `pickle` module must not be used to deserialize untrusted data because malicious payloads can execute code.

For a more secure implementation, consider authenticated key distribution, HTTPS, JSON or another safer serialization format, and appropriate error handling.

## Future Improvements

- [ ] Complete and test the full Alice-to-Bob messaging flow.
- [ ] Add `requirements.txt` and `.gitignore`.
- [ ] Replace `pickle` with a safer serialization format.
- [ ] Add input validation and structured error handling.
- [ ] Add automated tests for encryption, decryption, and tampering.
- [ ] Persist RSA keys securely instead of generating new ones on every restart.
- [ ] Add HTTPS and authenticated public-key distribution.
- [ ] Create a simple web interface for sending messages.
- [ ] Add a sequence diagram and screenshots demonstrating the workflow.

## Learning Outcomes

This project explores practical applications of cryptography, REST-style HTTP communication, Python development environments, and basic secure software design.

## Disclaimer

This repository is an educational project developed as part of an academic activity in Information Security and Auditing. It is not intended for protecting sensitive information in production environments.

## Author

**Lucas Lima Cavalcante**

Information Systems student | Python | Software Development | Information Security
