import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1",
    api_key=os.getenv("NEBIUS_API_KEY")
)

response = client.chat.completions.create(
    model="nvidia/nemotron-3-super-120b-a12b",
    messages=[
        {
            "role": "user",
            "content": "Grandma slept poorly last night and skipped breakfast. Give a short caregiver follow-up."
        }
    ],
    temperature=0.2,
    max_tokens=150
)

print(response.choices[0].message.content)