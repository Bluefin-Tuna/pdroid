from langchain.prompts import ChatPromptTemplate
from config import PROMPT_FOLDER
import os

def _read_prompt(name):
    if not os.path.isfile(f"{PROMPT_FOLDER}/{name}"):
        return None
    f = open(f"./{PROMPT_FOLDER}/{name}", "r")
    prompt = f.read()
    f.close()
    return prompt

class ProjectDroidPrompt():

    def __init__(self):
        self.system_prompt = _read_prompt("system.prompt")
        self.input_prompt = _read_prompt("input.prompt")

    def create_prompt(self):
        template = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("ai", "Done."),
            ("human", self.input_prompt),
        ])
        return template
