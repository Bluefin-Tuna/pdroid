"""File for loading in important environment and configuration variables for use throughout the application."""

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv(".env"))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PROMPT_FOLDER = os.getenv("PROMPT_FOLDER")