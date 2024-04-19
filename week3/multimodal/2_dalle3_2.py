import os
from openai import OpenAI
from PIL import Image
from io import BytesIO

# .envファイルからOPENAI_API_KEYを取得
openai_api_key = os.environ["OPENAI_API_KEY"]

# OpenAIクライアントを作成
client = OpenAI(api_key=openai_api_key)

# 入力画像を読み込む
image = Image.open("sunlit_lounge.png")
mask = Image.open("mask.png")

# 画像をRGBAフォーマットに変換
image = image.convert("RGBA")
mask = mask.convert("RGBA")

# 画像をバイト列に変換
image_bytes = BytesIO()
image.save(image_bytes, format='PNG')
image_bytes = image_bytes.getvalue()

mask_bytes = BytesIO()
mask.save(mask_bytes, format='PNG')
mask_bytes = mask_bytes.getvalue()

response = client.images.edit(
  model="dall-e-2",
  image=image_bytes,
  mask=mask_bytes,
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)

image_url = response.data[0].url
print(image_url)


