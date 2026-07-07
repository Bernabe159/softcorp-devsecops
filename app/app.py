"""
SoftCorp - Aplicación de demostración
Simula un microservicio corporativo simple para el laboratorio DevSecOps.
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)

# NOTA PEDAGÓGICA:
# En una app real, esta credencial NUNCA debe estar en texto plano.
# Este es un ejemplo intencional para que Gitleaks / Secret Scanning lo detecte
# durante la demo. En la versión "corregida" se reemplaza por Vault (ver vault_client.py)

@app.route("/")
def home():
    return jsonify({"servicio": "SoftCorp API", "estado": "activo"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
