import os
from openai import OpenAI

# .envファイルからOPENAI_API_KEYを取得
openai_api_key = os.environ["OPENAI_API_KEY"]

# OpenAIクライアントを作成
client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

