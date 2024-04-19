# 自動議事録生成システムの構築 - Whisper と GPT-4 を使用して

## はじめに

このチュートリアルでは、OpenAI の Whisper と GPT-4 モデルを活用して、自動議事録生成システムを開発します。このアプリケーションは、会議の音声を文字起こしし、議論の要約を提供し、重要なポイントとアクションアイテムを抽出し、感情分析を行います。

## クイックスタート

このチュートリアルでは、Python の基本的な理解と OpenAI API キーが必要です。提供された音声ファイルまたは独自の音声ファイルを使用できます。

また、python-docx と OpenAI ライブラリをインストールする必要があります。以下のコマンドを使用して、新しい Python 環境を作成し、必要なパッケージをインストールできます。

```bash
python -m venv env
source env/bin/activate
pip install openai
pip install python-docx
```

## プログラムを実行してみよう

### 例1: 音声の文字起こし

```python
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    # api_key="My API Key",
)

def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create("whisper-1", audio_file)
    return transcription['text']
```

この関数では、`audio_file_path` は文字起こしする音声ファイルへのパスです。この関数はファイルを開き、Whisper ASR モデル（whisper-1）に渡して文字起こしを行います。結果は生のテキストとして返されます。

### 例2: 文字起こしの要約と分析

```python
def meeting_minutes(transcription):
    abstract_summary = abstract_summary_extraction(transcription)
    key_points = key_points_extraction(transcription)
    action_items = action_item_extraction(transcription)
    sentiment = sentiment_analysis(transcription)
    return {
        'abstract_summary': abstract_summary,
        'key_points': key_points,
        'action_items': action_items,
        'sentiment': sentiment
    }
```

この関数では、`transcription` は Whisper から取得したテキストです。文字起こしは、4つの他の関数に渡すことができます。それぞれの関数は特定のタスクを実行するように設計されています。`abstract_summary_extraction` は会議の要約を生成し、`key_points_extraction` は主要なポイントを抽出し、`action_item_extraction` はアクションアイテムを特定し、`sentiment_analysis` は感情分析を実行します。

## 問題

<details>
<summary>問題1: Whisper モデルを使用して音声ファイルを文字起こしするために必要なものは何ですか？</summary>

a. 音声ファイルへのパス
b. 音声ファイル自体
c. 音声ファイルの URL
d. 音声ファイルの長さ

<details>
<summary>回答と解説</summary>

回答: b. 音声ファイル自体

`openai.Audio.transcribe` 関数は、ローカルまたはリモートサーバー上の音声ファイルへのパスではなく、実際の音声ファイル自体を渡す必要があります。つまり、音声ファイルを保存していないサーバー上でこのコードを実行している場合は、まず音声ファイルをそのデバイスにダウンロードする前処理ステップが必要です。

</details>
</details>

<details>
<summary>問題2: GPT-4 を使用してタスクを実行する最も効率的な方法は何ですか？</summary>

a. 各タスクに異なる関数を使用する
b. すべての命令を1つの関数に入れる
c. タスクごとに別々のモデルを使用する
d. タスクごとに異なる API を使用する

<details>
<summary>回答と解説</summary>

回答: b. すべての命令を1つの関数に入れる

チュートリアルでは、GPT-4 を使用して実行したい各タスクに異なる関数を使用しています。これはこのタスクを行う最も効率的な方法ではありません。これらの命令を1つの関数に入れることができますが、タスクを分割すると要約の品質が向上する可能性があります。

</details>
</details>

<details>