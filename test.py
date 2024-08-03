import httpx
import openai
import os
from dotenv import load_dotenv


load_dotenv()

proxy_url = os.getenv("PROXY_OPEN_AI")
apikey = os.getenv("OPENAI_API_KEY")


# # Настройка клиента httpx с прокси, если прокси указан
if proxy_url:
    client = httpx.Client(
        proxies={
            "http://": str(proxy_url),
            "https://": str(proxy_url),
        }
    )
else:
    client = httpx.Client()

# Настройка клиента OpenAI с использованием httpx клиента
openai.api_key = apikey
openai.aiosession.set(client)

# Запрос на создание чата
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.",
        },
        {
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming.",
        },
    ],
)

# Вывод результата
print(completion.choices[0].message["content"])
