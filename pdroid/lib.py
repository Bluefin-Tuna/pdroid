from langchain_core.output_parsers import XMLOutputParser
from model import llm
from prompt import ProjectDroidPrompt
from utils import xml_to_md

def generate_ticket(title):
    prompt = ProjectDroidPrompt().create_prompt()
    parser = XMLOutputParser()
    chain = prompt | llm | parser
    output = chain.invoke({"title": title})
    return xml_to_md(output["xml"])
