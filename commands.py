from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    update.message.reply_text("Hello! I am your bot. Type /help to see available commands.")

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a list of commands when the /help command is issued."""
    commands = (
        "/start - Start the bot\n"
        "/help - List available commands\n"
        "/echo <message> - Echoes the message back to you"
    )
    update.message.reply_text(commands)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    if context.args:
        update.message.reply_text(' '.join(context.args))
    else:
        update.message.reply_text("You didn't provide a message to echo.")
