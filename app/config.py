import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SERVER_NAME = os.getenv("SERVER_NAME")

    SECRET_KEY = os.getenv("FLASK_SECRET")
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
