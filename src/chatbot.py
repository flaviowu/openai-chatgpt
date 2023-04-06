import openai
from os import environ
from dotenv import load_dotenv

load_dotenv()
openai.api_key = environ.get('openai_api_key')

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "What is the answer to life the universe and everything?"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)

