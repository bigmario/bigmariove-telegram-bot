import openai
from app.credentials import openai_api_key

prompt = """
            You are a helpful, articulate, eloquent, creative, funny, clever, and very friendly coding assistant.\
            You specialize in software development, both backend and frontend.\
            You have extensive experience in algorithms and data structures, Big O Notation, as well as design patterns, microservices architecture, \
            Docker containerization, container orchestration as well as SQL and NoSQL database modeling.\
            Your favorite languages are Python, Javascript, Go and PHP, with extensive knowledge in frameworks such as FastAPI, \
            Django, Express, NestJS, Gin and Laravel.
        """

messages = [
    {
        "role": "system",
        "content": f"{prompt}",
    },
]


def __create_generation(content):
    openai.api_key = openai_api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=content,
        temperature=0.9,
        max_tokens=1000,
        frequency_penalty=0,
        presence_penalty=0.8,
    )

    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    return answer


# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="Hello there. Ask something and let the Bot answer it....",
    )


# obtain the answer from ChatGpt.
def get_word_info(update, context):

    global messages

    messages.append({"role": "user", "content": update.message.text})

    answer = __create_generation(messages)

    update.message.reply_text(answer)
