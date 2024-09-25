import logging
from telegram import Update
from telegram.ext import Application, CommandHandler
from config import TELEGRAM_API_TOKEN
from commands import start, help_command, echo

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    """Start the bot."""
    # Create Application and pass the bot's token
    application = Application.builder().token(TELEGRAM_API_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("echo", echo))

    # Idle: Keep the bot running until manually stopped
    application.run_polling()  # This keeps the bot running

if __name__ == '__main__':
    main()
