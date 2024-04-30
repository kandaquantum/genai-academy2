from fastapi import FastAPI                                                  # FastAPIをインポート

app = FastAPI()                                                               # FastAPIアプリケーションを作成

@app.get("/")                                                                 # ルートパス("/")へのGETリクエストを処理するエンドポイントを定義
def read_root():                                                              # - read_root関数を定義
    return {"Hello": "World"}                                                 # -- {"Hello": "World"}というJSONレスポンスを返す
