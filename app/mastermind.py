import openai
from app.credentials import openai_api_key


def __create_generation(update, prompt, start_sequence, restart_sequence):
    openai.api_key = openai_api_key

    prompt += update.message.text

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + start_sequence,
        temperature=0.9,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\nHuman:", "\n"],
    )

    answer = response.choices[0]["text"]
    new_prompt = prompt + start_sequence + answer + restart_sequence

    return answer, new_prompt


# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="Hello there. Ask something and let ChatGpt answer it....",
    )


# obtain the answer from ChatGpt.
def get_word_info(update, context):

    prompt = """The following is a conversation with an AI assistant. 
            The assistant is helpful, creative, funny, clever, and very friendly.
            Human: Hello, who are you?
            AI: I am an AI created by OpenAI. How can I help you today?
            Human:
         """

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    answer, prompt = __create_generation(
        update, prompt, start_sequence, restart_sequence
    )

    update.message.reply_text(answer)
