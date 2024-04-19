# GPT-4 with Vision 入門

## はじめに
GPT-4 with Vision (GPT-4V または gpt-4-vision-preview) は、画像を入力として受け取り、それについての質問に答えることができるモデルです。従来の言語モデルシステムは、テキストという単一の入力モダリティに制限されていましたが、GPT-4 with Vision は、画像という新しい入力モダリティを取り入れることで、GPT-4 の適用可能な領域を拡大しています。

## クイックスタート
画像をモデルに提供する主な方法は2つあります。1つは画像へのリンクを渡す方法、もう1つは base64 エンコードされた画像を直接リクエストに渡す方法です。以下は、画像 URL を使用した基本的な例です。

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What's in this image?"},
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

print(response.choices[0])
```

## プログラムを実行してみよう
次に、base64 エンコードされた画像を使用して、複数の画像を入力とするプログラムを実行してみましょう。

### 例1: 複数の画像を入力とする
```python
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What are in these images? Is there any difference between them?",
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
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
print(response.choices[0])
```

### 例2: 画像の詳細レベルを指定する
```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What's in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            "detail": "high"
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0].message.content)
```

## 問題
<details>
<summary>問題1: GPT-4 with Vision が医療画像の解釈に適していない理由は？</summary>

a. 医療画像のサイズが大きすぎるため
b. 医療画像の色が複雑すぎるため
c. 医療画像の解釈には専門知識が必要なため
d. 医療画像のフォーマットに対応していないため

<details>
<summary>回答と解説</summary>

回答: c. 医療画像の解釈には専門知識が必要なため

GPT-4 with Vision は、CT スキャンなどの専門的な医療画像の解釈には適していません。医療アドバイスのために使用すべきではありません。医療画像の正確な解釈には、専門的な知識と経験が必要です。
</details>
</details>

<details>
<summary>問題2: GPT-4 with Vision が苦手とする画像の種類は？</summary>

a. 回転した画像
b. 高解像度の画像
c. カラー画像
d. 正方形の画像

<details>
<summary>回答と解説</summary>

回答: a. 回転した画像

GPT-4 with Vision は、回転した画像や上下逆さまのテキストや画像を誤って解釈する可能性があります。モデルは、画像の向きに敏感であり、標準的な向きからずれていると正確に理解できない場合があります。
</details>
</details>

<details>
<summary>問題3: GPT-4 with Vision が画像を処理するためのトークンコストを決定する2つの要因は？</summary>

a. 画像のサイズと色
b. 画像のサイズと詳細オプション
c. 画像の形式と詳細オプション
d. 画像の形式とサイズ

<details>
<summary>回答と解説</summary>

回答: b. 画像のサイズと詳細オプション

画像の入力は、テキスト入力と同様に、トークンで計測され、課金されます。特定の画像のトークンコストは、そのサイズと各 image_url ブロックの detail オプションの2つの要因によって決定されます。
</details>
</details>