import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    BOT_USER_NAME = os.getenv("BOT_USER_NAME")
    URL = os.getenv("URL")
    SECRET_KEY = os.getenv("FLASK_SECRET")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    MONGO_URI = os.getenv("MONGO_URI")
