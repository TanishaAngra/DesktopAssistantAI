import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to hr applying for entry-level software developer role?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n\nSubject: Application\n\nDear [Name],\n\nI am writing this letter to apply for the Software Engineer position at your company. I have recently graduated with a degree in Computer Science. I have done some projects in college and I know programming languages like Java, Python, and C++. I am looking for a job where I can use my skills.\n\nSincerely,\n[Your Name]"
    }
  ],
  "created": 1683815400,
  "id": "cmpl-7F1aqg7BkzIY8vBnCxYQh8Xp4wO85",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 125,
    "prompt_tokens": 9,
    "total_tokens": 134
  }
}
'''