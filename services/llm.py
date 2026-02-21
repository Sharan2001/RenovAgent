from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OpenAI"))

def call_model(system_prompt, history):

    messages = [{"role": "system", "content": system_prompt}]

    for h in history:
        messages.append(h)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.7
    )

    return response.choices[0].message.content