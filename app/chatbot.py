import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

async def get_chatbot_response(message: str) -> str:
    try:
        # Make the API call using the older openai.ChatCompletion format
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=150
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        raise ValueError(f"Error generating response: {str(e)}")
