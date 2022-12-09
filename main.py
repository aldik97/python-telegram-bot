import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CallbackContext, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: CallbackContext.bot):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot please talk to me!")


async def echo(update: Update, context: CallbackContext.bot):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# async def caps(update: Update, context: CallbackContext.bot):
#     text_caps = ' '.join(context.args).upper()
#     await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


if __name__ == '__main__':
    application = ApplicationBuilder().token('2031212165:AAGyIdKaE-Zl7rO7XaQZr1CX1BUnTIh7lAk').build()

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    start_handler = CommandHandler('start', start)
    # caps_handler = CommandHandler('caps', caps)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    # application.add_handler(caps_handler)

    application.run_polling()
