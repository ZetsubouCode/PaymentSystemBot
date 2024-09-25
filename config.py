import os
import json
from cryptography.fernet import Fernet

def load_key():
    """Load the encryption key from a secure place (environment or file)."""
    # In production, it's better to store this in an environment variable or a secret manager
    with open('key.key', 'rb') as key_file:
        return key_file.read()

def load_config():
    """Load and decrypt the configuration from the encrypted JSON file."""
    key = load_key()  # Load the encryption key
    cipher_suite = Fernet(key)

    # Load the encrypted config file
    with open('encrypted_config.json', 'r') as json_file:
        encrypted_config = json.load(json_file)

    # Decrypt the data
    decrypted_config = {
        key: cipher_suite.decrypt(value.encode()).decode() for key, value in encrypted_config.items()
    }

    return decrypted_config

# Load the decrypted configuration
config = load_config()

TELEGRAM_API_TOKEN = config.get("TELEGRAM_API_TOKEN")

# Ensure the token and password are loaded correctly
if not TELEGRAM_API_TOKEN:
    raise ValueError("Config data is missing or decryption failed.")
