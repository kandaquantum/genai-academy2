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

# 画像URLをダウンロードしてPNGファイルとして保存する
import requests

# 画像URLからファイル名を取得
filename = image_url.split("/")[-1]

# 画像をダウンロード
response = requests.get(image_url)

# PNGファイルとして保存
with open(filename, "wb") as f:
    f.write(response.content)

print(f"画像を {filename} として保存しました")


