import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


if __name__ == '__main__':
    application = ApplicationBuilder().token('2031212165:AAGyIdKaE-Zl7rO7XaQZr1CX1BUnTIh7lAk').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()