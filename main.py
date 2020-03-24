from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from answer_generator import generate_answer


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Ask me something!')


def generate(update, context):
    """Echo the user message."""
    update.message.reply_text(generate_answer(update.message.text))


def main():
    """Start bot"""
    updater = Updater("paste ur bot token", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, generate))

    updater.start_polling()
    updater.idle()


# if __name__ == '__main__':
#     main()
