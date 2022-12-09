import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent, Update
from telegram.ext import InlineQueryHandler, CallbackContext, ApplicationBuilder, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def inline_caps(update: Update, context: CallbackContext.bot):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


async def unknown(update: Update, context: CallbackContext.bot):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


if __name__ == '__main__':
    application = ApplicationBuilder().token('2031212165:AAGyIdKaE-Zl7rO7XaQZr1CX1BUnTIh7lAk').build()

    inline_caps_handler = InlineQueryHandler(inline_caps)
    application.add_handler(inline_caps_handler)

    # Other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)

    application.run_polling()
