# ChatGPT Interface

A Python interface for interacting with ChatGPT via web interface using Selenium.

## Installation

```
pip install chatgpt_interface
```

## Usage

```python
from chatgpt_interface import ChatGPTInterface

chatgpt = ChatGPTInterface()
chatgpt.open_chat("URL_of_ChatGPT_Web_Interface")
chatgpt.send_prompt("Hello, how are you?")
response = chatgpt.get_response()
print(response)
chatgpt.close()
```
