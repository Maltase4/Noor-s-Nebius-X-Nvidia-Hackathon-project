import os
from openai import OpenAI
from dotenv import load_dotenv

# Load your secret API key from the .env file
load_dotenv()
api_key = os.getenv("NEBIUS_API_KEY")

# Connect to Nebius Token Factory using the OpenAI-compatible SDK
client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=api_key
)

def ask_ai(messages_history):
    """Sends text conversation history to Nebius and returns the AI's reply."""
    try:
        response = client.chat.completions.create(
            model="nvidia/Nemotron-3.5-Super-VL",  # NVIDIA open-source model hosted on Nebius
            messages=messages_history,
            temperature=0.9
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Nebius cloud: {e}"