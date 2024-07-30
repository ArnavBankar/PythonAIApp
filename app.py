import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Get OpenAI API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

def get_openai_response(api_key, messages):
    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=messages
    )
    return response.choices[0].message.content

# Streamlit app
def main():
    st.set_page_config(page_title="Arnav's Sick Chatbot", page_icon="🤖")
    
    st.title("Arnav's Sick Chatbot 🤖")

    if not api_key:
        st.error("OpenAI API key not found. Please set it in your .env file.")
        return

    # Sidebar
    st.sidebar.title("Settings")
    temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
    
    # User input and chat history
    user_message = st.text_input("Enter your message:")
    chat_history = st.empty()

    if st.button("Send"):
        if user_message:
            # Define initial messages
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]

            # Get OpenAI response
            response_content = get_openai_response(api_key, messages)
            
            # Display the conversation
            chat_history.markdown(f"**User:** {user_message}\n\n**Assistant:** {response_content}")

            # Optionally clear input
            user_message = ""

if __name__ == "__main__":
    main()
