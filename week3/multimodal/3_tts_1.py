import os
from openai import OpenAI
from pathlib import Path

# .envファイルからOPENAI_API_KEYを取得
openai_api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

def generate_speech(text, voice="shimmer", filename="speech.mp3"):
    """
    指定されたテキストから音声を生成し、ファイルに保存する関数
    
    Parameters:
    text (str): 音声に変換するテキスト
    voice (str): 使用するボイス。デフォルトは"shimmer"
    filename (str): 保存するファイル名。デフォルトは"speech.mp3"
    
    Returns:
    None
    """
    speech_file_path = Path(__file__).parent / filename
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text
    )
    response.stream_to_file(speech_file_path)
    print(f"{filename}に音声ファイルを保存しました。")
    
    # 生成した音声ファイルを開く
    os.system(f"open {speech_file_path}")

def generate_multilingual_speech(texts):
    """
    複数の言語のテキストから音声を生成し、ファイルに保存する関数
    
    Parameters:
    texts (dict): 言語をキー、テキストを値とする辞書
    
    Returns:
    None
    """
    for lang, text in texts.items():
        filename = f"{lang}.mp3"
        generate_speech(text, voice="alloy", filename=filename)
        
        # 生成した音声ファイルを開く
        speech_file_path = Path(__file__).parent / filename
        os.system(f"open {speech_file_path}")
        
        # 音声の再生が終了するまで待機
        input(f"{lang}の音声が終了したらEnterキーを押してください...")

if __name__ == "__main__":
    # 日本語のテキストから音声を生成
    japanese_text = "こんにちは！今日はとてもいい天気で、元気いっぱいです。何か新しいことを始めるのに最適な日ですね！"
    generate_speech(japanese_text)
    
    # 複数の言語のテキストから音声を生成
    multilingual_texts = {
        "en": "This is a test of the multilingual capabilities of the OpenAI TTS API.",
        "es": "Esta es una prueba de las capacidades multilingües de la API de TTS de OpenAI.",
        "fr": "Ceci est un test des capacités multilingues de l'API TTS d'OpenAI.",
        "de": "Dies ist ein Test der mehrsprachigen Fähigkeiten der OpenAI TTS API.",
        "ja": "これはOpenAI TTS APIの多言語機能のテストです。"
    }
    generate_multilingual_speech(multilingual_texts)

