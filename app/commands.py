from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from .mastermind import create_generation, messages


# set up the introductory statement for the bot when the /start command is invoked
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="Hello there. How can i help your coding adventure today?",
    )


# obtain the answer from ChatGpt mastermind.
def get_word_info(update: Update, context: CallbackContext):
    global messages

    messages.append({"role": "user", "content": update.message.text})

    answer = create_generation(messages)

    update.message.reply_text(answer)


def showMenu(update: Update, context: CallbackContext):
    """
    method to handle the /start command and create keyboard
    """

    # defining the keyboard layout
    kbd_layout = [["Option 1", "Option 2"], ["Option 3", "Option 4"], ["Option 5"]]

    # converting layout to markup
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html
    kbd = ReplyKeyboardMarkup(kbd_layout)

    # sending the reply so as to activate the keyboard
    update.message.reply_text(text="Select Options", reply_markup=kbd)


def removeMenu(update: Update, context: CallbackContext):
    """
    method to handle /remove command to remove the keyboard and return back to text reply
    """

    # making a reply markup to remove keyboard
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html
    reply_markup = ReplyKeyboardRemove()

    # sending the reply so as to remove the keyboard
    update.message.reply_text(text="I'm back.", reply_markup=reply_markup)
    pass
