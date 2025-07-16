from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up OpenAI API key (assuming you are using OpenAI GPT)

async def get_chatbot_response(message: str) -> str:
    try:
        # Correct usage of the ChatCompletion API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # specify the model
            messages=[{"role": "user", "content": message}],  # specify the messages
            max_tokens=150
        )
        return response.choices[0].message.content.strip()  # access the response content
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        raise ValueError(f"Error generating response: {str(e)}")
