# Project Droid

## Overview

### Goal
The goal of this challenge was to take in a basic task description (title) and create a well-scoped industry standard ticket for Jira, Linear, etc...

### Approach
To do this I created a simple Flask server to take in the title. With this information I prompted GPT-4 with the prompts specified in `./pdroid/prompts` and reformatted the response. This response was then served to the end user for easy copy pasting.

## Walkthrough

### Configuration
Before getting started with the environment creation and running the server for usage, you need to setup the .env with the correct characteristics so it can be easily used. In a text editor of your choice, open the .env file in the project root directory. You'll notice 2 environment variables. You can leave the PROMPT_FOLDER environment variable as is. For the OPENAI_API_KEY, you'll need to replace the {INSERT API KEY HERE} with a valid key from OpenAI. If you need instructions for how to get this API key, I'd suggest following the **Account Setup** portion of this quickstart [guide](https://platform.openai.com/docs/quickstart) from OpenAI. After that is done feel free to move onto the next step.

### Environment
For this project, Anaconda (specifically MiniConda) was the environment manager of choice. If this is not installed refer to this [link](https://docs.anaconda.com/free/anaconda/install/index.html). After that is done, you can run `conda env create -f requirements.yml`. After the environment is created and enabled (to enable it run the following command `conda activate PDroid`), run `pip install -e .`, `pip install openai` and `pip install langchain-core` to ensure no issues at runtime.

### Runtime
In order to run the application, from the root project directory run this command `cd pdroid`. From there you can run `python app.py` and the flask server will startup. There will be instructions given in the console/terminal about where the application is being hosted (usually **127.0.0.1:5000**). Open that in a browser of your choice and begin using! Have fun!