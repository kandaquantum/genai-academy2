# テキスト生成AIの概要

## 目次
- [はじめに](#introduction)
- [テキスト生成AIとは](#text-generation-ai)
- [APIとローカルLLMの違いと分類](#api-vs-local-llm)
- [テキスト生成AIモデルの分類と主要モデルの紹介](#text-generation-models)
- [GPTとClaudeの概要と応用例](#gpt-and-claude)

<a id="introduction"></a>
## はじめに
近年、自然言語処理の分野で大きな進歩を遂げているテキスト生成AI。本講義では、テキスト生成AIの概要、主要なモデルとその特徴、APIとローカルLLMの違いなどについて学びます。これらの知識を活用することで、文書執筆の効率化を図ることができるでしょう。

<a id="text-generation-ai"></a>
## テキスト生成AIとは
テキスト生成AIは、大量のテキストデータを学習し、新しいテキストを生成するAIモデルです。これらのモデルは、自然言語処理タスク、コンテンツ生成、対話システムの開発など、幅広い分野で応用されています。テキスト生成AIの登場により、人間の文書執筆作業の効率化や自動化が可能になりつつあります。

<a id="api-vs-local-llm"></a>
## APIとローカルLLMの違いと分類
テキスト生成AIモデルは、APIを通じて利用するものとローカルで実行可能なものに分類できます。

| 分類 | 特徴 | 例 |
|------|------|------|
| API経由 | クラウド上のサーバーでモデルを実行し、APIを通じて結果を取得 | GPT-4, Claude|
| ローカルLLM | ユーザーのデバイス上でモデルを実行 | Llama, Mistral, CohereのCommand R+  |

<a id="text-generation-models"></a>
## テキスト生成AIモデルの分類と主要モデルの紹介

### GPT-4
#### 詳細解説
GPT-4は、OpenAIによる大規模トランスフォーマーモデルです。膨大な量のテキストデータを学習し、自然言語処理タスクに広く利用されています。GPT-4は、その前身であるGPT-3と比較して、より高度な言語理解と生成能力を持っています。

#### 例題と解説
```python
import openai  # openaiライブラリをインポート

openai.api_key = "YOUR_API_KEY"  # APIキーを設定

from openai import OpenAI  # OpenAIクラスをインポート

client = OpenAI()  # OpenAIクライアントを初期化

# GPT-4モデルを使用してチャットの完了を作成
stream = client.chat.completions.create(
    model="gpt-4",  # 使用するモデルを指定
    messages=[{"role": "user", "content": "Say this is a test"}],  # ユーザーのメッセージを指定
    stream=True,  # ストリームモードを有効にする
)
for chunk in stream:  # ストリームからチャンクを取得するたびにループ
    if chunk.choices[0].delta.content is not None:  # チャンクにコンテンツが含まれているか確認
        print(chunk.choices[0].delta.content, end="")  # コンテンツを出力
```
上記のPythonコードは、OpenAIのAPIを使用してGPT-4にプロンプトを与え、テキストを生成する例です。`prompt`変数に与えられた文章の続きを、GPT-4が生成します。

### Claude
#### 詳細解説
Claudeは、Anthropicが開発したテキスト生成AIモデルです。倫理的ガイドラインに基づくテキスト生成を特徴としており、有害なコンテンツや偏見を含むテキストの生成を抑制するように設計されています。また、特定のドメインや言語スタイルに合わせたカスタマイズが可能です。

#### 例題と解説
```python
import anthropic
import os
from dotenv import load_dotenv
from graphviz import Digraph  # graphvizモジュールをインポート

load_dotenv()  # .envファイルから環境変数を読み込む

anthropic.api_key = os.getenv("ANTHROPIC_API_KEY")  # 環境変数からAPI keyを取得

def generate_syllabus(transcript):
    """
    文字起こし情報からカリキュラムを作成する関数
    
    Args:
        transcript (str): 文字起こし情報
        
    Returns:
        str: カリキュラム
    """
    client = anthropic.Anthropic(api_key=anthropic.api_key)
    
    prompt = f"""
    以下の文字起こし情報からカリキュラムを作成してください。
    カリキュラムはyaml形式で出力してください。

    
    文字起こし情報:
    {transcript}
    
    - week: 1
     topics:
     - 基礎開発ツール講習
     lectures:
       - title: （複数）
       description: |
    - week: 2
     topics:
     - 
     lectures:
       - title: （複数）
       description: |
         
    """
    
    # Anthropic APIを使用してClaudeモデルにプロンプトを送信し、レスポンスを取得する
    response = client.messages.create(
        model="claude-3-opus-20240229",  # 使用するClaudeモデルのバージョンを指定
        max_tokens=4000,  # 生成するトークンの最大数を設定
        temperature=0.7,  # 生成時のランダム性を制御するtemperature値を設定
        messages=[
            {
                "role": "user",  # ユーザーからのメッセージであることを示す
                "content": [
                    {
                        "type": "text",  # メッセージのタイプがテキストであることを示す
                        "text": prompt  # プロンプトの内容を指定
                    }
                ]
            }
        ]
    )
    
    # レスポンスからシラバスのYAML部分を抽出し、不要な部分を削除する
    syllabus_yaml = response.content[0].text.strip()  # レスポンスのテキスト部分を取得し、前後の空白を削除
    syllabus_yaml = syllabus_yaml.replace("```yaml", "").replace("```", "")  # YAMLのコードブロック記法を削除
    return syllabus_yaml

```
上記のPythonコードは、AnthropicのAPIを使用してClaudeにプロンプトを与え、テキストを生成する例です。`prompt`変数に与えられたテーマに基づいて、Claudeが短編小説を生成します。
