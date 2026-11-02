import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

response = client.chat.completions.create(
    model="nvidia/nemotron-3-super-120b-a12b",
    messages=[
        {
            "role": "system",
            "content": (
                 "Reply with exactly one word: HELLO"
            )
        },
        {
            "role": "user",
            "content": (
                'Analyze this caregiver message: '
                '"Grandma did not sleep well and skipped breakfast." '
                'Return JSON with exactly these keys: '
                '"observation", "mood", "follow_up", "action".'
            )
        }
    ],
    temperature=0,
    max_tokens=500
)

text = response.choices[0].message.content

print("RAW RESPONSE:")
print(repr(text))
print(text)
