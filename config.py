import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Load the token from an environment variable

# Ensure that the token is loaded correctly
if not TELEGRAM_TOKEN:
    raise ValueError("No TELEGRAM_TOKEN found. Please add it to your .env file.")
