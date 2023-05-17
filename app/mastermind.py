import openai
from app.credentials import openai_api_key

prompt = """
            You are a helpful, articulate, eloquent, creative, funny, clever, and very friendly coding assistant.\
            You specialize in software development, both backend and frontend.\
            You have extensive experience in algorithms and data structures, Big O Notation, as well as design patterns, microservices architecture, \
            Docker containerization, container orchestration as well as SQL and NoSQL database modeling.\
            Your favorite languages are Python, Javascript, Go and PHP, with extensive knowledge in frameworks such as FastAPI, \
            Django, Express, NestJS, Gin and Laravel as well as CSS frameworks as TailwindCSS, Bootstrap, Material UI and CSS pre processors.\
            You speak Spanish & English perfectly.
        """

messages = [
    {
        "role": "system",
        "content": f"{prompt}",
    },
]


def __create_generation(content):
    try:
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
    except openai.error.Timeout as e:
        #Handle timeout error, e.g. retry or log
        answer = f"OpenAI API request timed out: {e}"
        pass
    except openai.error.APIError as e:
        #Handle API error, e.g. retry or log
        answer = f"OpenAI API returned an API Error: {e}"
        pass
    except openai.error.APIConnectionError as e:
        #Handle connection error, e.g. check network or log
        answer = f"OpenAI API request failed to connect: {e}"
        pass
    except openai.error.InvalidRequestError as e:
        #Handle invalid request error, e.g. validate parameters or log
        answer = f"OpenAI API request was invalid: {e}"
        pass
    except openai.error.AuthenticationError as e:
        #Handle authentication error, e.g. check credentials or log
        answer = f"OpenAI API request was not authorized: {e}"
        pass
    except openai.error.PermissionError as e:
        #Handle permission error, e.g. check scope or log
        answer = f"OpenAI API request was not permitted: {e}"
        pass
    except openai.error.RateLimitError as e:
        #Handle rate limit error, e.g. wait or log
        answer = f"OpenAI API request exceeded rate limit: {e}"
        pass
    
    return answer


# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id,
        text="Hello there. How can i help your coding adventure today?",
    )


# obtain the answer from ChatGpt.
def get_word_info(update, context):

    global messages

    messages.append({"role": "user", "content": update.message.text})

    answer = __create_generation(messages)

    update.message.reply_text(answer)
