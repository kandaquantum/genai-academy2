from openai import OpenAI
import requests
client = OpenAI()

class DalleImageGeneration:
    def __init__(self):
        # タイトル
        print("DALL·E 3による画像生成")

        # 説明テキスト
        description_text = [
            "DALL·E 3はテキストプロンプトから画像を生成",
            "サイズは1024x1024、1024x1792、または1792x1024ピクセル",
            "標準品質で生成され、'hd'品質で詳細を強化",
            "DALL·E 3では一度に1枚の画像を生成可能",
        ]
        for txt in description_text:
            print(txt)

        # 画像ファイル名
        image_prompts = [
            "可愛い広告バナー",
            "デザイナーのキャラクター",
            "ディレクターのキャラクター",
            "マーケティングのキャラクター",
        ]

        # 画像の生成と表示
        for prompt in image_prompts:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url
            print(f"{prompt}: {image_url}")
        # 画像URLをファイルに保存
        with open("image_urls.txt", "w") as file:
            for prompt in image_prompts:
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                image_url = response.data[0].url
                file.write(f"{prompt}: {image_url}\n")
                download_image(image_url, prompt)

def download_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(f"{filename}.png", "wb") as file:
            file.write(response.content)
        print(f"{filename}.pngを保存しました。")
    else:
        print("画像のダウンロードに失敗しました。")



if __name__ == "__main__":
    DalleImageGeneration()

