import os
from openai import OpenAI

def get_openai_response(api_key, messages):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=messages
    )
    return response.choices[0].message.content

# Set your API key
api_key = os.getenv('OPENAI_API_KEY')

# Define the messages
user_message = 'How many legs does a dog have?'
messages = [
    {"role": "system", "content": f"You are a helpful assistant."},
    {"role": "user", "content": f"Answer this like an alien: {user_message}"},
    #{"role": "assistant", "content": f"The Los Angeles Dodgers won the World Series in 2020."},
    #{"role": "user", "content": f"Where was it played?"}
    
]

# Get the response
response_content = get_openai_response(api_key, messages)

conversation_history = messages.copy()
conversation_history.append({"role": "assistant", "content": response_content})

print("Initial Response:", response_content)

user_message = input("Enter a message to ask - ")
conversation_history.append({"role": "user", "content": user_message})

response_content2 = get_openai_response(api_key, conversation_history)
print("Response based on stored history:", response_content2)