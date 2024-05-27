<h1 align="center">AgenPy 0.1.2 📦</h1>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)

A python package for setting up agentic behavior for LLMs. Includes optimization for large training data, and adherence to applied interactional policies.

## Table Of Contents

- [Features](#features)
- [Usage](#usage)
  - [Starter Code for OpenAI](#starter-code-openai)
- [Donate](#donate--help)

## Features

AgenPy is particularly useful for creating multi-modal agents using LLMs and other AI tools.

- <strong>Set Behavior & Actions:</strong><br>
Using various APIs, an agent with particular persona can be created. Users can set their behaviors and reactions to different scenarios. User can also set up different tasks to perform according to needs.

- <strong>Database Management:</strong><br>
Import your knowledge base for extended information to the agent. Is organized into vector databases for ease of recall, hence faster and optimized response rates.

## Usage

Import this package into Python using this command. [Here](https://pypi.org/project/agenpy/) is the PyPI website for more details.

```shell
pip install agenpy
```

### Starter Code (OpenAI)

Here is a starter code to understand how to use the AgenPy library properly. Create a file named `demo.py` and paste the following code into it.

```python
import asyncio
from agenpy import agent

async def run_async_demo():
    bot = agent.SimpleOpenAIAgent(api_key="your-openai-api-key", is_async=True)
    bot.message_log.append({"role": "user", "content": "Tell me a joke."})

    print("Streaming async response:")
    async for chunk in bot.stream():
        print(chunk, end='')

def run_sync_demo():
    bot = agent.SimpleOpenAIAgent(api_key="your-openai-api-key", is_async=False)
    bot.message_log.append({"role": "user", "content": "Tell me a joke."})

    print("Streaming sync response:")
    for chunk in bot.stream():
        print(chunk, end='')

if __name__ == "__main__":
    print("Running async demo:")
    asyncio.run(run_async_demo())

    print("\n\nRunning sync demo:")
    run_sync_demo()
```

Edit the keys in the given code such that they are your OpenAI API keys. To execute this code, run the command:

```shell
python demo.py
```

## Donate & Help

If you want to help in the maintenance of this package and keep it open and free for everyone, consider making a donation. It's optional, but we'll be grateful if you did. All of the donations go straight into the development of this package only.<br>
|   Crypto Network   |     Wallet     |
|:------------------:|:--------------:|
|![Bitcoin](https://img.shields.io/badge/Bitcoin-000?style=for-the-badge&logo=bitcoin&logoColor=white)|`bc1qppcjpkcpsrxc35z9zcqcdvtzk333qslc9ft32j`|
|![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)|`0xc1a9A83fE19a37e362652D9Ca6b7cA12fF3E875d`|