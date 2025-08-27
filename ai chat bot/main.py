import openai
import os
from openai import OpenAI

key = "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"



client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)