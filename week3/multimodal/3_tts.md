# OpenAI TTS APIを使ってテキストから音声を生成する

## はじめに

OpenAI Audio APIは、テキストから自然な音声を生成するためのエンドポイントを提供します。6つの組み込みボイスが用意されており、以下のような用途に使用できます。

- ブログ記事の朗読
- 複数の言語で音声を生成
- ストリーミングを使ってリアルタイムで音声を出力

## クイックスタート

音声エンドポイントには、モデル、音声に変換するテキスト、音声生成に使用するボイスの3つの主要な入力があります。シンプルなリクエストは次のようになります。

```python
from pathlib import Path  # Pathライブラリをインポートして、ファイルパスの操作を簡単にします📁
from openai import OpenAI  # OpenAIライブラリからOpenAIクラスをインポートします
client = OpenAI()  # OpenAIクライアントを初期化します🌟

speech_file_path = Path(__file__).parent / "speech.mp3"  # 現在のファイルのディレクトリに"speech.mp3"という名前で保存するパスを設定します🎵
response = client.audio.speech.create(
  model="tts-1",  # モデルを"tts-1"に設定します🔊
  voice="nova",  # ボイスを"nova"に設定します🗣️
  input="こんにちは！今日はとてもいい天気で、元気いっぱいです。何か新しいことを始めるのに最適な日ですね！"  # 音声に変換したいテキストを入力します📝
)

response.stream_to_file(speech_file_path)  # 応答をファイルにストリーミングして保存します💾
```

このコードを実行するには、以下の手順を実行します。

1. OpenAIのAPIキーを取得し、環境変数`OPENAI_API_KEY`に設定します。
2. 必要なライブラリをインストールします: `pip install openai`
3. 上記のコードを`speech.py`などのファイルに保存します。
4. コマンドラインから`python speech.py`を実行します。

デフォルトでは、エンドポイントはMP3形式の音声ファイルを出力しますが、サポートされている他の形式に設定することもできます。

## プログラムを実行してみよう

### 例1: 異なるボイスで音声を生成する

```python
from pathlib import Path
from openai import OpenAI
client = OpenAI()

voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]

for voice in voices:
    speech_file_path = Path(__file__).parent / f"{voice}.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input="This is a test of the different voices available in the OpenAI Audio API."
    )
    response.stream_to_file(speech_file_path)
```

### 例2: 異なる言語で音声を生成する

```python
from pathlib import Path
from openai import OpenAI
client = OpenAI()

texts = {
    "en": "This is a test of the multilingual capabilities of the OpenAI Audio API.",
    "es": "Esta es una prueba de las capacidades multilingües de la API de audio de OpenAI.",
    "fr": "Ceci est un test des capacités multilingues de l'API audio d'OpenAI.",
    "de": "Dies ist ein Test der mehrsprachigen Fähigkeiten der OpenAI Audio API.",
    "ja": "これはOpenAI Audio APIの多言語機能のテストです。"
}

for lang, text in texts.items():
    speech_file_path = Path(__file__).parent / f"{lang}.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)
```

## 問題

<details>
<summary>1. OpenAI Audio APIの組み込みボイスの数は？</summary>

- [ ] 4
- [x] 6
- [ ] 8
- [ ] 10

OpenAI Audio APIには6つの組み込みボイス（alloy, echo, fable, onyx, nova, shimmer）が用意されています。
</details>

<details>
<summary>2. OpenAI Audio APIのデフォルトの出力フォーマットは？</summary>

- [x] MP3
- [ ] WAV
- [ ] FLAC
- [ ] AAC

OpenAI Audio APIのデフォルトの出力フォーマットはMP3ですが、他のフォーマット（opus, aac, flac, pcm）にも対応しています。
</details>

<details>
<summary>3. OpenAI Audio APIでサポートされていない機能は？</summary>

- [ ] 複数の言語で音声を生成
- [ ] ストリーミングを使ってリアルタイムで音声を出力
- [x] カスタムボイスの作成
- [ ] 生成された音声ファイルの所有権

OpenAI Audio APIでは、ユーザー独自のカスタムボイスを作成することはできません。
</details>