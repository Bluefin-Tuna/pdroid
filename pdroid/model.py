from langchain.chat_models import ChatOpenAI
from config import OPENAI_API_KEY

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0, max_tokens=2048)