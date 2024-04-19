# 環境構築手順


1. Pythonのインストール

2. OpenAI APIキーの取得
   - OpenAIのウェブサイト（https://beta.openai.com/signup/）でアカウントを作成します。
   - APIキーを取得します。取得方法は以下の通りです。
     - ダッシュボードにログインします。
     - 右上のメニューから「API keys」を選択します。
     - 「Create new secret key」をクリックして新しいAPIキーを生成します。
   - 取得したAPIキーは環境変数として設定します。

3. 必要なPythonライブラリのインストール
   - 以下のコマンドを実行して、必要なライブラリをインストールします。
     ```
     pip install openai
     ```
4. .envファイルの設定
   - プロジェクトのルートディレクトリに`.env`ファイルを作成します。
   - `.env`ファイルに以下の内容を記述します。
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - `your_api_key_here`の部分を、取得したOpenAI APIキーに置き換えます。
   - `.env`ファイルはgitignoreに追加して、APIキーが漏洩しないように注意しましょう。
   - Pythonコード内で`os.environ["OPENAI_API_KEY"]`を使ってAPIキーを読み込むことができます。

以上で、OpenAI APIを使うための環境構築は完了です。APIキーを設定したら、必要なライブラリをインストールして、サンプルコードを実行してみましょう。APIの使い方や注意点については、以降の講義で詳しく説明します。

サンプル

```python
import os
from openai import OpenAI
openai_api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "この画像は何ですか？"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)
```