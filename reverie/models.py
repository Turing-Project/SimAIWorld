"""
allow different model API
"""

from litellm import completion
import os

## set ENV variables
os.environ["OPENAI_API_KEY"] = "openai key"
os.environ["COHERE_API_KEY"] = "cohere key"
os.environ["ANTHROPIC_API_KEY"] = "anthropic key"

messages = [{"content": "Hello, how are you?", "role": "user"}]

# openai call
response = completion(model="gpt-3.5-turbo", messages=messages)

# cohere call
response = completion(model="command-nightly", messages=messages)

# anthropic
response = completion(model="claude-2", messages=messages)
