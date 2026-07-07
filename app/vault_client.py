"""
SoftCorp - Integración con HashiCorp Vault (Bóveda de Secretos)
================================================================
Esta es la VERSIÓN CORREGIDA de app.py: en vez de tener la credencial
escrita en el código (texto plano), la aplicación la solicita a Vault
en tiempo de ejecución (inyección dinámica de secretos).

Requisitos previos (en tu máquina o VM):
    1. Vault corriendo en modo dev:
       docker run --cap-add=IPC_LOCK -d --name vault-dev \
         -p 8200:8200 \
         -e 'VAULT_DEV_ROOT_TOKEN_ID=root-token-demo' \
         hashicorp/vault

    2. Guardar el secreto de ejemplo dentro de Vault:
       docker exec -it vault-dev vault kv put secret/softcorp/db \
         password="ClaveSuperSeguraDesdeVault123"

    3. Instalar el cliente de Python:
       pip install hvac
"""
import os
import hvac
from flask import Flask, jsonify

app = Flask(__name__)

VAULT_ADDR = os.environ.get("VAULT_ADDR", "http://127.0.0.1:8200")
VAULT_TOKEN = os.environ.get("VAULT_TOKEN", "root-token-demo")


def obtener_password_desde_vault():
    """Conecta a Vault y obtiene la credencial en tiempo real (no hardcodeada)."""
    client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)

    if not client.is_authenticated():
        raise Exception("No se pudo autenticar contra Vault")

    secreto = client.secrets.kv.v2.read_secret_version(
        path="softcorp/db",
        mount_point="secret",
    )
    return secreto["data"]["data"]["password"]


@app.route("/")
def home():
    return jsonify({"servicio": "SoftCorp API", "estado": "activo", "secretos": "gestionados por Vault"})


@app.route("/demo-vault")
def demo_vault():
    """
    Endpoint SOLO para la demostración en vivo: muestra que la contraseña
    se obtiene de Vault, NO está escrita en el código fuente.
    """
    try:
        password = obtener_password_desde_vault()
        # Se muestra parcialmente enmascarada para no exponerla en pantalla
        enmascarada = password[:3] + "*" * (len(password) - 3)
        return jsonify({"origen": "HashiCorp Vault", "password_obtenida": enmascarada})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
