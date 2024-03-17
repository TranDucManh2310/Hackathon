import os
from openai import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2023-05-15"
)

message = "Bạn bao nhiêu tuổi ?"
def get_bot_response(message):
    response = client.chat.completions.create(
        model="GPT35TURBO16K",
        messages=[
            {"role": "system", "content": "Bạn là 1 giáo viên, và bạn trả lời bằng tiếng Việt"},
            {"role": "user", "content": message},
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return response.choices[0].text.strip()
