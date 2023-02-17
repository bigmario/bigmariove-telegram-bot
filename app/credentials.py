import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("BOT_TOKEN")  # "place your token here"
bot_user_name = os.environ.get("BOT_USER_NAME")  # "bot username"
URL = os.environ.get("URL")  # "the heroku app link that we will create later"
openai_api_key = os.environ.get("OPENAI_API_KEY")
port = os.environ.get("PORT", 5001)
host = os.environ.get("HOST", "0.0.0.0")
