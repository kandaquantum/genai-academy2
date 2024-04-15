
from openai import OpenAI

import os  # osライブラリをインポートします。
from dotenv import load_dotenv  # dotenvからload_dotenv関数をインポートします。
from openai import OpenAI

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
load_dotenv()  # .envファイルから環境変数を読み込みます。
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "あなたは詩的なアシスタントであり、複雑なプログラミングの概念を創造的な才能で説明するのが得意です。"},
    {"role": "user", "content": "プログラミングにおける再帰の概念を説明する詩を作成してください。"}
  ]
)

print(completion.choices[0].message.content)
