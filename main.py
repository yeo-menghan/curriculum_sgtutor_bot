import os
from langchain.chat_models import ChatOpenAI


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YourKey")
