# OpenAI Embeddings入門

OpenAIのEmbeddingsを使うと、テキストをベクトル表現に変換し、検索や分類などの様々なタスクに活用できます。このガイドでは、EmbeddingsAPIの基本的な使い方を学びます。

## Embeddingsとは

Embeddingsは、テキスト間の関連性を測るための数値表現です。主に以下のような用途で使われます。

- 検索（クエリとの関連性でランク付け）
- クラスタリング（類似テキストのグループ化）
- レコメンデーション（関連テキストを持つアイテムの推薦）
- 異常検知（関連性の低い外れ値の特定）
- 多様性の測定（類似度分布の分析）
- 分類（最も類似するラベルへのテキストの分類）

Embeddingは、浮動小数点数のベクトル（リスト）で表現されます。2つのベクトル間の距離が近いほど関連性が高く、遠いほど関連性が低いことを示します。

## Embeddingsの取得方法

EmbeddingsAPIエンドポイントにテキストとモデル名（例: `text-embedding-3-small`）を送信すると、Embeddingベクトルが返されます。このベクトルを抽出し、ベクトルデータベースに保存して様々な用途に活用できます。

```python
from openai import OpenAI
client = OpenAI()

response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)
```

デフォルトでは、Embeddingベクトルの長さは`text-embedding-3-small`で1536、`text-embedding-3-large`で3072になります。`dimensions`パラメータを指定することで、ベクトルの次元数を減らすことができます。

## Embeddingモデル

OpenAIは2つの強力な第3世代Embeddingモデル（モデルIDに`-3`を含む）を提供しています。

| モデル                     | 1ドルあたりのページ数 | MTEBでの性能 | 最大入力トークン |
|----------------------------|----------------------|-------------|-----------------|
| text-embedding-3-small     | 62,500               | 62.3%       | 8191            |
| text-embedding-3-large     | 9,615                | 64.6%       | 8191            |
| text-embedding-ada-002     | 12,500               | 61.0%       | 8191            |

## ユースケース

Amazonのレビューデータセットを使って、いくつかの代表的なユースケースを見ていきます。

### Embeddingsの取得

レビューの要約とテキストを結合し、単一のEmbeddingベクトルに変換します。

```python
from openai import OpenAI
client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

df['ada_embedding'] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
df.to_csv('output/embedded_1k_reviews.csv', index=False)
```

### Embeddingの次元削減

より大きなEmbeddingを使うと、一般的にコストや計算量、メモリ、ストレージの消費が増えます。`dimensions`パラメータを使うことで、Embeddingの性能を維持しつつ、サイズを削減できます。

```python
from openai import OpenAI
import numpy as np

client = OpenAI()

def normalize_l2(x):
    x = np.array(x)
    if x.ndim == 1:
        norm = np.linalg.norm(x)
        if norm == 0:
            return x
        return x / norm
    else:
        norm = np.linalg.norm(x, 2, axis=1, keepdims=True)
        return np.where(norm == 0, x, x / norm)


response = client.embeddings.create(
    model="text-embedding-3-small", input="Testing 123", encoding_format="float"
)

cut_dim = response.data[0].embedding[:256]
norm_dim = normalize_l2(cut_dim)

print(norm_dim)
```

### Embeddingを使った質問応答

モデルのコンテキストウィンドウに追加情報を入れることで、ユーザーの質問に対する回答の生成を改善できます。ただし、これはトークンコストを増加させます。Embeddingベースの検索を使うことで、このトレードオフを探ることができます。

```python
query = f"""Use the below article on the 2022 Winter Olympics to answer the subsequent question. If the answer cannot be found, write "I don't know."

Article: 
\"\"\"
{wikipedia_article_on_curling}
\"\"\"

Question: Which athletes won the gold medal in curling at the 2022 Winter Olympics?"""

response = client.chat.completions.create(
    messages=[
        {'role': 'system', 'content': 'You answer questions about the 2022 Winter Olympics.'},
        {'role': 'user', 'content': query},
    ],
    model=GPT_MODEL,
    temperature=0,
)

print(response.choices[0].message.content)
```

以上がEmbeddingsの基本的な使い方です。テキストを数値表現に変換することで、検索や分類など様々な用途に活用できます。次元削減や追加情報の利用など、ユースケースに合わせて柔軟に調整していきましょう。