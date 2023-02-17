import os
import openai
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from app.credentials import bot_token
from main import get_info

telegram_bot_token = bot_token

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="Hello there. Ask something and let ChatGpt answer it....",
    )


# obtain the information of the word provided and format before presenting.
def get_word_info(update, context):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"],
    )

    update.message.reply_text(response)


# run the start function when the user invokes the /start command
dispatcher.add_handler(CommandHandler("start", start))

# invoke the get_word_info function when the user sends a message
# that is not a command.
dispatcher.add_handler(MessageHandler(Filters.text, get_word_info))
# updater.start_polling()
updater.start_webhook(
    listen="0.0.0.0",
    port=int(os.environ.get("PORT", 5001)),
    url_path=telegram_bot_token,
    webhook_url=os.environ.get("URL") + telegram_bot_token,
)