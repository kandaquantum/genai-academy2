import os
from openai import OpenAI

# .envファイルからOPENAI_API_KEYを取得
openai_api_key = os.environ["OPENAI_API_KEY"]

# OpenAIクライアントを作成
client = OpenAI(api_key=openai_api_key)

def transcribe_audio(audio_file_path):
    """
    音声ファイルを文字起こしする関数
    
    Parameters:
    audio_file_path (str): 文字起こしする音声ファイルへのパス
    
    Returns:
    str: 文字起こしされたテキスト
    """
    with open(audio_file_path, 'rb') as audio_file:
        # Transcriptions.create()メソッドの引数を修正
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="verbose_json",
            timestamp_granularities=["word"]
        )
    return transcription.text  # 'text'属性を使ってテキストを取得

def abstract_summary_extraction(transcription):
    """
    文字起こしから会議の要約を生成する関数
    
    Parameters:
    transcription (str): 文字起こしされたテキスト
    
    Returns:
    str: 生成された会議の要約
    """
    # OpenAIのAPIを使って文字起こしから要約を生成
    response = client.completions.create(
        model="gpt-4",
        prompt=f"以下は会議の文字起こしです。この会議の要約を3文程度で生成してください:\n\n{transcription}\n\n要約:",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    summary = response.choices[0].text.strip()
    return summary
def key_points_extraction(transcription):
    """
    文字起こしから主要なポイントを抽出する関数
    
    Parameters:
    transcription (str): 文字起こしされたテキスト
    
    Returns:
    list: 抽出された主要なポイントのリスト
    """
    # OpenAIのAPIを使って文字起こしから主要なポイントを抽出
    response = client.completions.create(
        engine="text-davinci-002",
        prompt=f"以下は会議の文字起こしです。この会議の主要なポイントを3点程度で箇条書きで教えてください:\n\n{transcription}\n\n主要なポイント:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    key_points_text = response.choices[0].text.strip()
    key_points = key_points_text.split("\n")
    return key_points

def action_item_extraction(transcription):
    """
    文字起こしからアクションアイテムを特定する関数（ダミー）
    """
    return ["アクション1", "アクション2"]

def sentiment_analysis(transcription):
    """
    文字起こしに対して感情分析を実行する関数（ダミー）
    """
    return "ポジティブ"

def meeting_minutes(transcription):
    """
    文字起こしから議事録を生成する関数
    
    Parameters:
    transcription (str): 文字起こしされたテキスト
    
    Returns:
    dict: 議事録の各要素を含む辞書
    """
    # 文字起こしから会議の要約を抽出
    abstract_summary = abstract_summary_extraction(transcription)
    # 文字起こしからキーポイントを抽出
    key_points = key_points_extraction(transcription)
    # 文字起こしからアクションアイテムを抽出
    action_items = action_item_extraction(transcription)
    # 文字起こしに対して感情分析を実行
    sentiment = sentiment_analysis(transcription)
    return {
        'abstract_summary': abstract_summary,
        'key_points': key_points,
        'action_items': action_items,
        'sentiment': sentiment
    }

if __name__ == "__main__":
    # サンプルの音声ファイルを文字起こし
    audio_file_path = "speech.mp3"
    transcription = transcribe_audio(audio_file_path)
    print(f"文字起こし結果: {transcription}")
    
    # # 文字起こしから議事録を生成
    # minutes = meeting_minutes(transcription)
    # print(f"議事録: {minutes}")
