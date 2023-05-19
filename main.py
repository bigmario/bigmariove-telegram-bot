from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from app import bot_token, port, URL, host
from app import start, get_word_info, showMenu, removeMenu

telegram_bot_token = bot_token

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


# run the start function when the user invokes the /start command
dispatcher.add_handler(CommandHandler("start", start))

# run the showMenu function when the user invokes the menu command
dispatcher.add_handler(CommandHandler("menu", showMenu))

# run the removeMenu function when the user invokes the remove-menu command
dispatcher.add_handler(CommandHandler("remove", removeMenu))

# invoke the get_word_info function when the user sends a message
# that is not a command.
dispatcher.add_handler(MessageHandler(Filters.text, get_word_info))


# updater.start_polling()
updater.start_webhook(
    listen=host,
    port=int(port),
    url_path=telegram_bot_token,
    webhook_url=URL + telegram_bot_token,
)
