from flask import Flask, request
import telegram
from app.credentials import bot_token, bot_user_name, URL
from app.mastermind import get_response

from app import create_app

from app.config import Config

global bot
global TOKEN
TOKEN = bot_token

bot = telegram.Bot(token=TOKEN)


app = create_app()


@app.route("/{}".format(TOKEN), methods=["POST"])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode("utf-8").decode()
    print("got text message :", text)

    response = get_response(text)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return "ok"


@app.route("/setwebhook", methods=["GET", "POST"])
async def set_webhook():
    s = await bot.setWebhook("{URL}{HOOK}".format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route("/")
def index():
    return "."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
