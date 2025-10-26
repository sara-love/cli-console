from openai import OpenAI
from anthropic import Anthropic
from google import genai
from xai_sdk import Client
from xai_sdk.chat import user, system
from dotenv import load_dotenv
import os

load_dotenv()

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
xai_client = Client(api_key=os.getenv("XAI_API_KEY"))
gemini_client = genai.Client()

def openai_chat_response(model: str, message: str):
    result = openai_client.responses.create(    
        model="gpt-5",
        input=message,
        reasoning={"effort": "low"},
        text={"verbosity": "low"},
    )

    return result.output_text

def anthropic_chat_response(query: str):
    result = anthropic_client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": query}
        ],
    )

    return result.content[0].text

def gemini_chat_response(query: str):
    result = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=query,
    )
    return result.text

def grok_chat_response(query: str):
    chat = xai_client.chat.create(
        model="grok-4")

    chat.append(user(query))

    result = chat.sample()
    return result