import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config import TELEGRAM_TOKEN
from commands import start, help_command, echo

# Set up logging to monitor the bot's activity and errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')

def main() -> None:
    """Start the bot."""
    # Create an Updater object to handle bot updates
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("echo", echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot (polling)
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
