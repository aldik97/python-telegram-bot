import telegram.ext

with open('token.txt', 'r') as f:
    TOKEN = f.read()

def start(update,context):
    update.message.reply_text("Hello! Welcome to LatihanBot")

def greetings(update,context):
    update.message.reply_text("Aloha brother")


updater = telegram.ext.Updater(TOKEN, update_queue=0)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("greetings", greetings))

updater.start_polling()
updater.idle()
