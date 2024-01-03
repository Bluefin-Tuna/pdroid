"""File for loading and constructing prompts used by Project Droid."""

from langchain.prompts import ChatPromptTemplate
from config import PROMPT_FOLDER
import os

def _read_prompt(name):
    """Helper function for reading in prompt file from prompt folder."""
    if not os.path.isfile(f"{PROMPT_FOLDER}/{name}"):
        return None
    f = open(f"./{PROMPT_FOLDER}/{name}", "r")
    prompt = f.read()
    f.close()
    return prompt

class ProjectDroidPrompt():

    """Class for creating and structuring prompts for use with LLMs like GPT-4"""

    def __init__(self):
        self.system_prompt = _read_prompt("system.prompt")
        self.input_prompt = _read_prompt("input.prompt")

    def create_prompt(self):
        """Function for creating prompt chain template for data input"""
        template = ChatPromptTemplate.from_messages([
            ("system", self.system_prompt),
            ("ai", "Done."),
            ("human", self.input_prompt),
        ])
        return template
