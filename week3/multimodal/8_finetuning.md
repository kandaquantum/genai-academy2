[# OpenAI Embeddings入門

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
# OpenAI Fine-tuning入門

OpenAIのFine-tuningを使うと、事前学習済みのモデルをカスタマイズし、特定のタスクに特化したモデルを作成できます。このガイドでは、Fine-tuningの基本的な使い方を学びます。

## Fine-tuningの利点

Fine-tuningには以下のような利点があります。

- プロンプトによる学習よりも高品質な結果が得られる
- プロンプトに収まる以上の例を使って学習できる
- プロンプトが短くなることでトークン使用量を節約できる
- 低レイテンシーでリクエストできる

## Fine-tuning可能なモデル

現在、以下のモデルがFine-tuningに対応しています。

- gpt-3.5-turbo-0125（推奨）
- gpt-3.5-turbo-1106
- gpt-3.5-turbo-0613
- babbage-002
- davinci-002
- gpt-4-0613（実験的）

## Fine-tuningの手順

Fine-tuningは大まかに以下の手順で行います。

1. 学習データの準備とアップロード
2. Fine-tuningジョブの作成
3. 結果の評価と必要に応じて手順1に戻る
4. Fine-tuningされたモデルの使用

## 学習データの準備

学習データは、Chat Completions APIと同じ形式のメッセージリストとして準備します。各メッセージは役割（`system`, `user`, `assistant`）とテキスト（`content`）を持ちます。例えば以下のようなデータセットを作成します。

```json
{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}
{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who wrote 'Romeo and Juliet'?"}, {"role": "assistant", "content": "Oh, just some guy named William Shakespeare. Ever heard of him?"}]}
{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "How far is the Moon from Earth?"}, {"role": "assistant", "content": "Around 384,400 kilometers. Give or take a few, like that really matters."}]}
```

## 学習データのアップロード

学習データは、Files APIを使ってアップロードします。

```python
from openai import OpenAI
client = OpenAI()

client.files.create(
  file=open("mydata.jsonl", "rb"),
  purpose="fine-tuning"
)
```

## Fine-tuningジョブの作成

学習データをアップロードしたら、Fine-tuningジョブを作成します。

```python
from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-abc123", 
  model="gpt-3.5-turbo"
)
```

`model`には、Fine-tuningの対象となるモデルを指定します。`training_file`には、アップロードした学習データのファイルIDを指定します。

Fine-tuningジョブの進行状況は、`list`, `retrieve`, `cancel`, `list_events`メソッドで確認できます。

## Fine-tuningされたモデルの使用

Fine-tuningジョブが成功すると、`fine_tuned_model`フィールドにカスタムモデルの名前が設定されます。このモデルは、Chat Completions APIやCompletions APIで使用できます。

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo:my-org:custom_suffix:id", 
  messages=[
    {"role": "system", "content": "You are a helpful assistant."}, 
    {"role": "user", "content": "Hello!"}
  ]
)
print(completion.choices[0].message)
```

## Fine-tuningの反復

Fine-tuningの結果が期待通りでない場合は、以下のような方法で学習データを調整します。

- 残る問題を対象とする例を追加する
- 既存の例の問題点を精査する
- データのバランスと多様性を考慮する
- 学習例に回答に必要な情報がすべて含まれていることを確認する
- 学習例の一貫性を確認する
- 学習例が推論時と同じ形式であることを確認する

また、学習データの量を増やすことで、モデルのパフォーマンスを向上させることもできます。

## ハイパーパラメータの調整

Fine-tuningでは、以下のハイパーパラメータを指定できます。

- エポック数（`n_epochs`）
- 学習率（`learning_rate_multiplier`）
- バッチサイズ（`batch_size`）

デフォルト値から始め、必要に応じて調整することをお勧めします。

```python
from openai import OpenAI
client = OpenAI()

client.fine_tuning.jobs.create(
  training_file="file-abc123",
  model="gpt-3.5-turbo",
  hyperparameters={
    "n_epochs": 2
  }
)
```

以上が、Fine-tuningの基本的な使い方です。特定のタスクに特化したモデルを作成することで、より高品質な結果を効率的に得ることができます。学習データとハイパーパラメータを反復的に調整し、最適なモデルを構築していきましょう。
response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)

print(response.data\[0\].embedding)
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
   return client.embeddings.create(input = \[text\], model=model).data\[0\].embedding

df\['ada_embedding'\] = df.combined.apply(lambda x: get_embedding(x, model='text-embedding-3-small'))
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

cut_dim = response.data\[0\].embedding\[:256\]
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
    messages=\[
        {'role': 'system', 'content': 'You answer questions about the 2022 Winter Olympics.'},
        {'role': 'user', 'content': query},
    \],
    model=GPT_MODEL,
    temperature=0,
)

print(response.choices\[0\].message.content)
```

以上がEmbeddingsの基本的な使い方です。テキストを数値表現に変換することで、検索や分類など様々な用途に活用できます。次元削減や追加情報の利用など、ユースケースに合わせて柔軟に調整していきましょう。](7_embedding.md)