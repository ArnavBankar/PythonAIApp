import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Set the OpenAI API key
openai.api_key = api_key

def describe_image(messages):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=300,
    )
    return response['choices'][0]['message']['content']

image = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
question = "What's in this image?"

messages = [
    {
        "role": "user",
        "content": question,
    },
    {
        "role": "system",
        "content": f"<img src='{image}' />",
    }
]

response = describe_image(messages)
print(response)
