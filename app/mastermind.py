import openai
from app.credentials import openai_api_key


# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="Hello there. Ask something and let ChatGpt answer it....",
    )


# obtain the answer from ChatGpt.
def get_word_info(update, context):
    openai.api_key = openai_api_key

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=update.message.text,
        temperature=0.6,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=1,
        presence_penalty=1,
    )

    message = f"{response.choices[0].text}"

    update.message.reply_text(message)
