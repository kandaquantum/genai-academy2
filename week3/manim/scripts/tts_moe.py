from pathlib import Path
from openai import OpenAI
client = OpenAI()

speech_file_path = Path(__file__).parent / "speech_moe.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="nova",
  input="""
Mixture of Experts、略してエムオーイーは、複数の専門家モデルを組み合わせたアーキテクチャです。
入力データは各エキスパートに渡され、それぞれが独自の出力を生成します。
同時にゲーティング関数が各専門家モデルの出力を重み付けし、最終的な出力を決定します。

例えば、可愛い広告バナーを作成する際には、マーケター、デザイナー、ライターといった専門家が協力します。
各専門家がアイデアを出し合い、ディレクターがそれらを取捨選択し、最適な広告バナーを生み出すのです。
"""
)


response.stream_to_file(speech_file_path)