from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token='1156757253:AAG86TW2qYpW1jjYFYDSRADrzGxRv8pw6HI', use_context=True)

dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="How can i help you?")
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def rules(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="5 Simple Rules\n1) No leaching\n2) No Promoting other\n 3) ")
start_handler = CommandHandler('rules', rules)
dispatcher.add_handler(start_handler)

updater.start_polling()