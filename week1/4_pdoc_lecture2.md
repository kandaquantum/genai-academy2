# ドキュメントプログラミング基礎

## 目次
- [はじめに](#introduction)
- [ドキュメントプログラミングとは](#what-is-document-programming)
- [Pythonでのドキュメントプログラミング](#document-programming-in-python)
  - [コメントの重要性](#importance-of-comments)
  - [docstringの活用](#using-docstrings)
  - [コード例と解説](#python-code-example)
- [自然言語プログラミング](#natural-language-programming)
  - [自然言語プログラミングの概要](#overview-of-nlp)
  - [自然言語プログラミングの利点](#advantages-of-nlp)
  - [コード例と解説](#nlp-code-example)
  - [自然言語プログラミングのワークフロー](#natural-language-programming-workflow)
- [まとめ](#conclusion)

<a id="introduction"></a>
## はじめに
ドキュメントプログラミングは、プログラムの可読性と保守性を向上させるための重要な手法です。本講義では、ドキュメントプログラミングの基本的な概念と応用例を学びます。

本講義では、これらのドキュメントプログラミングの種類について、具体的な例を交えながら詳しく解説していきます。受講者の皆さんには、ドキュメントプログラミングの重要性を理解し、実際のプログラミングで活用できるようになることを目指します。
<a id="what-is-document-programming"></a>
## ドキュメントプログラミングとは
ドキュメントプログラミングとは、プログラムコードにドキュメント（説明文）を組み込むことで、コードの理解を容易にし、保守性を高める手法です。ドキュメントプログラミングには大きく分けて2種類あります。

1. 一般的なプログラミングにおいて、コードの各行に自然言語（日本語など）の説明を加える方法
2. 完全に自然言語のみでドキュメントを記述し、内部的に他のプログラミング言語（JavaScriptなど）に変換される方法


1つ目は、Pythonなどの一般的なプログラミング言語を用いる際に、コードの各行に自然言語（日本語など）の説明を加える方法です。これにより、コードの意図や機能が明確になり、他の開発者がコードを理解しやすくなります。特に、大規模なプロジェクトや長期的なメンテナンスが必要な場合に効果的です。

2つ目は、自然言語のみでドキュメントを記述し、内部的に他のプログラミング言語（JavaScriptなど）に変換される方法です。この方法では、プログラミングの知識がなくても、自然言語で処理の手順を記述することができます。これにより、ドメインの専門家とプログラマーの協力がスムーズになり、開発の効率化が期待できます。具体的なツールとして[create.xyz](https://www.create.xyz/)などがあります。

<a id="document-programming-in-python"></a>
## Pythonでのドキュメントプログラミング

<a id="importance-of-comments"></a>
### コメントの重要性
Pythonでのドキュメントプログラミングにおいて、コメントは重要な役割を果たします。コメントを適切に使用することで、コードの理解を助け、保守性を高めることができます。

<a id="using-docstrings"></a>
### docstringの活用
Pythonではdocstringと呼ばれる特別なコメントを使用して、関数やクラス、モジュールの説明を記述することができます。docstringは関数やクラスの定義直後に記述し、トリプルクォート（"""）で囲みます。

<a id="python-code-example"></a>
### コード例と解説
以下は、Pythonでのドキュメントプログラミングの例です。

#### 数の性質を花屋さんに教える

数の「性質」を判断する関数を定義します。まるで花の種類を分類するように、数も分類します。
- 条件分岐を含む問題
プロンプト
```
"整数がもし数が100より大きいなら、特大の数、正の数であれば'正の数です'、負の数であれば'負の数です'、0であれば'ゼロです'と出力する。"
このプログラムを書いてください。1行1行コメントアウトの記載をお願いします。
私は花屋なので、私にわかりやすく説明してください。
```

```python
def classify_number(number):
    # もし数が100より大きいなら、特大の数と判断します。まるで巨大な樹木のようですね。
    if number > 100:
        return '特大です'
    # もし数が0より大きい（ポジティブ）なら、正の数と判断します。まるで太陽に向かって伸びる花のようですね。
    elif number > 0:
        return '正の数です'
    # もし数が0より小さい（ネガティブ）なら、負の数と判断します。まるで根が地中深くに伸びる植物のようです。
    elif number < 0:
        return '負の数です'
    # もし数が0と等しいなら、「ゼロです」と判断します。これはまるで、種がまだ芽を出していない状態ですね。
    else:
        return 'ゼロです'

# いくつかの「数」をテストして、その「性質」を判定します。まるで、異なる花の種類を識別するように。
test_numbers = [200, 10, -5, 0]
# test_numbersリストの各要素に対して、classify_number関数を適用します。
# その結果を新しいリストにまとめます。まるで、花束を作るように数の性質を集めているイメージです。
results = [classify_number(num) for num in test_numbers]
# 最終的な判定結果を出力します。まるで、花束の中のそれぞれの花の種類を確認するように、各数の性質（正の数、負の数、ゼロ）がわかります。
print(results)

```


以下のコード例では、生徒の点数のリストから平均点を計算しています。以下の手順で処理を行っています。


プロンプト
```
テストの平均点を出すためのプログラムを書いてください。
1行1行コメントアウトの記載をお願いします。
```

```python
def calculate_average(scores):
    """
    与えられた数値のリストの平均値を計算する関数です。
    
    引数:
    scores (list): 数値のリスト
    
    返り値:
    float: 計算された平均値
    """
    # 合計値を計算するための変数を初期化します。
    total = 0
    
    # リスト内の各数値に対してループ処理を行います。
    for score in scores:
        # 現在の数値を合計値に加算します。
        total += score
    
    # リストの要素数を取得します。
    count = len(scores)
    
    # 平均値を計算します。合計値を要素数で割ります。
    average = total / count
    
    return average

# 使用例
# 生徒の点数のリストを定義します。
scores = [80, 90, 75, 85, 95]
# calculate_average関数を呼び出して平均点を計算します。
average_score = calculate_average(scores)
# f-stringを使って平均点を出力します。
print(f"平均点は{average_score}点です。")
```

この例では、`calculate_average`関数にdocstringを使用して、関数の説明、引数、戻り値について記述しています。また、コメントを使用して、コードの使用例を示しています。

このコード例は、リストの要素に対するループ処理、合計値の計算、平均値の計算といった基本的なプログラミングの概念を示しています。これらの概念は、様々なプログラミングの場面で応用することができます。

例えば、このコードを応用して、生徒の点数を入力として受け取り、平均点を計算するプログラムを作成することができます。また、条件分岐を追加して、平均点に応じて異なるメッセージを出力することもできます。

プログラミングを学ぶ際は、このようなシンプルなコード例から始めて、徐々に複雑なプログラムへと発展させていくことが重要です。コード例を理解し、応用することで、プログラミングのスキルを向上させることができます。

<a id="natural-language-programming"></a>
## 自然言語プログラミング

<a id="overview-of-nlp"></a>
### 自然言語プログラミングの概要
自然言語プログラミングは、自然言語のみを使用してプログラムを記述する手法です。自然言語で記述されたドキュメントは、内部的に他のプログラミング言語に変換されて実行されます。

<a id="advantages-of-nlp"></a>
### 自然言語プログラミングの利点
自然言語プログラミングの主な利点は、プログラミングの知識がなくても、ドキュメントを記述できることです。これにより、ドメイン専門家やエンドユーザーが直接プログラムを作成できるようになります。

<a id="nlp-code-example"></a>
### コード例と解説
以下は、自然言語プログラミングの例です。

```
料金ページの仕様:

1. 全体の設定
   - モダンなデザイン
   - 背景を白に
   - テキストをInterフォントに
   - レスポンシブデザイン

2. タイトル
   - ページ上部に「シンプルで透明性のある、誰にでも分かりやすい料金体系」というテキストを追加
   - タイトルを太字に

3. プラン別の設定
   - 各プランのタイトル（スタータープラン、プロプラン、ビジネスプラン）を中央揃えで小さいフォントサイズに
   - タイトルの下に画像を追加（全て同じサイズに調整し、切れないように表示）
   - 価格（$19/月、$59/月、$149/月）を中央揃えに
   - 説明文（個人向け、など）を価格の下に移動
   - 箇条書きを左揃えに

4. ボタンとアイコン
   - 「プランを選択」ボタンを、#2849F4のアウトラインと#2849F4のテキストを持つ透明なボタンに
   - 「営業担当に連絡する」ボタンを#2849F4の背景に白いテキストに
   - 緑のチェックマークを全て#2849F4に
   - 赤い「x」を薄いグレーのアウトラインと薄いグレーの「x」に、背景は透明に

これらの仕様に従って、モダンでユーザーフレンドリーな料金ページを作成してください。
```

以下は、自然言語プログラミングを用いて生成された料金ページの例です。

![自然言語プログラミングで生成された料金ページの例](./images/createxyz.png)

この例では、自然言語で記述された仕様をもとに、モダンでユーザーフレンドリーな料金ページが自動生成されています。自然言語プログラミングを活用することで、プログラミングの知識がなくても、desired outputに近いWebページを作成することができます。



この例では、自然言語のみを使用して、商品一覧を表示するプログラムの仕様を記述しています。この仕様をもとに、内部的にJavaScriptなどのプログラミング言語に変換され、実行されます。



<a id="natural-language-programming-workflow"></a>
### 自然言語プログラミングのワークフロー
自然言語プログラミングを効果的に行うためのワークフローは以下のようになります。

1. 自然言語でプログラムの仕様を記述する
   - 目的とする処理や機能を自然言語で詳細に記述します。
   - 例えば、「ユーザーがフォームに入力した情報をデータベースに保存し、確認メールを送信する」といった具合です。

2. 自然言語の仕様を元に、プログラムを生成する
   - 自然言語処理技術を用いて、自然言語の仕様からプログラムコードを自動生成します。
   - 必要に応じて、生成されたコードを修正・調整します。

3. ドキュメントプログラミングの手法を適用する
   - 生成されたプログラムコードに、自然言語の説明（コメント）を追加します。
   - コードの各部分の意図や機能を明確にし、可読性を高めます。

4. コメントを抽出してドキュメントを作成する
   - プログラムコードからコメントのみを抽出します。
   - 抽出したコメントを整理し、独立したドキュメントを作成します。

5. ドキュメントを修正する
   - 作成したドキュメントを元に、プログラムコードの一部を修正します。
   - 修正時に生成されたコメントを、ドキュメントに追加します。
   - これにより、コードとドキュメントの整合性が保たれ、プログラムの理解が深まります。

この一連のワークフローにより、自然言語の仕様からプログラムコードを生成し、さらにドキュメントプログラミングの手法を適用することで、可読性の高いドキュメントとプログラムを同時に作成することができます。自然言語プログラミングとドキュメントプログラミングを組み合わせることで、プログラミングの効率化と品質向上を図ることができるのです。


具体例

```python
def generate_syllabus_graph(syllabus):
    """
    syllabusの内容からグラフを生成する関数
    
    Args:
        syllabus (dict): syllabusの内容が入った辞書
        
    Returns:
        None
    """
    client = anthropic.Anthropic(api_key=anthropic.api_key)
    
    prompt = f"""
    syllabus:
    {syllabus}

    上記のシラバスから、
    以下のPythonコードを生成してください。

    # syllabusデータの作成 （型：リスト[dict]）
    # Graphvizを使ってグラフを作成。コメントに'Syllabus Graph'を指定。
    # 週のボックスノードと講義サブボックスの作成
    # syllabusデータの各週について繰り返し処理
    # 週のインデックスを取得
    # 週のトピックを取得し、カンマ区切りの文字列に変換
    # 週のノード名を作成（例: "Week 1\n基礎開発ツール講習"）
    # 週のノードを作成。ボックス形状、塗りつぶし、水色の背景色を指定。
    # 週ごとのサブグラフを作成
    # 講義のタイトルをリストアップし、改行区切りの文字列に変換
    # サブグラフ内に講義一覧のノードを作成。ボックス形状、ラベルに講義一覧を指定。
    # 週のノードと講義一覧のノードを破線で接続
    # 週ボックスノードの下部（south）からエッジを始め、headport='sw'はサブグラフの左下（south-west）にエッジを接続するように指定
    # 隔週ごとの矢印の接続
    # syllabusデータの週の数-1回繰り返し処理
    # 現在の週のデータを取得
    # 次の週のデータを取得
    # 現在の週のノード名を作成
    # 次の週のノード名を作成
    # 現在の週のノードと次の週のノードを矢印で接続
    # グラフの保存と表示
    # グラフを'syllabus_graph'という名前で保存し、表示する

    pythonのコードブロックのみ出力。その他説明は書かないこと。
    """
    
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=2000,
        temperature=0.7,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    
    code = response.content[0].text.strip()
    
    code = code.replace("```python", "").replace("```", "")
    with open("generate_syllabus_graph.py", "w") as f:
        f.write(code)

    # codeを実行するコードを追記
    exec(code)
    
    
# from generate_syllabus_graph import generate_syllabus_graph

```

以下実装結果

```python


import graphviz

syllabus = [{'index': 1, 'topics': ['基礎開発ツール講習'], 'lectures': [{'title': 'テキスト生成AIの概要', 'description': 'テキスト生成AIについて概要を説明する\n'}, {'title': 'GPTを使ったオリジナルチャットボットの作成', 'description': 'GPTを使ってオリジナルのチャットボットを作る方法を教える\n'}, {'title': 'Cursorの基本的な使い方と活用法', 'description': 'Cursorの基本的な使い方と、どんなことに活用できるのかをレクチャーする\n'}]}, {'index': 2, 'topics': ['応用開発ツール講習'], 'lectures': [{'title': 'テキスト生成AIの概要（応用編）', 'description': 'テキスト生成AIの概要を説明する（応用編）\n'}, {'title': 'GPTを使った独自のチャットボット作成（応用編）', 'description': 'GPTを使った独自のチャットボット作成について深掘りする\n'}, {'title': 'Cursorの実践的な操作方法と活用法', 'description': 'Cursorのより実践的な操作方法と活用法について学ぶ\n'}]}, {'index': 3, 'topics': ['AIを使った自動化ツールの作成'], 'lectures': [{'title': 'RPA(Robotic Process Automation)の概要', 'description': 'RPA(Robotic Process Automation)の概要を説明する\n'}, {'title': 'PythonとNode.jsを使った自動化スクリプトの書き方', 'description': 'PythonやNode.jsを使った自動化スクリプトの書き方を解説する\n'}, {'title': '自動化ツールの実践的な運用方法', 'description': '作成したツールの実践的な運用方法について触れる\n'}]}]

graph = graphviz.Digraph(comment='Syllabus Graph')

for week in syllabus:
    week_index = week['index']
    week_topics = ', '.join(week['topics'])
    week_node_name = f"Week {week_index}\n{week_topics}"
    graph.node(week_node_name, shape='box', style='filled', fillcolor='lightblue')
    
    with graph.subgraph(name=f'cluster_week_{week_index}') as subgraph:
        lecture_titles = '\n'.join([lecture['title'] for lecture in week['lectures']])
        subgraph.node(f'lectures_{week_index}', shape='box', label=lecture_titles)
        graph.edge(week_node_name, f'lectures_{week_index}', style='dashed', tailport='s', headport='sw')

for i in range(len(syllabus) - 1):
    current_week = syllabus[i]
    next_week = syllabus[i + 1]
    current_week_node_name = f"Week {current_week['index']}\n{', '.join(current_week['topics'])}"
    next_week_node_name = f"Week {next_week['index']}\n{', '.join(next_week['topics'])}"
    graph.edge(current_week_node_name, next_week_node_name)

graph.view(filename='syllabus_graph', cleanup=True)


```

<a id="conclusion"></a>
## まとめ
本講義では、ドキュメントプログラミングの基本的な概念と応用例について学びました。Pythonでのドキュメントプログラミングでは、コメントとdocstringを活用することで、コードの可読性と保守性を高めることができます。また、自然言語プログラミングでは、自然言語のみでプログラムを記述することができ、ドメイン専門家やエンドユーザーが直接プログラムを作成できるようになります。ドキュメントプログラミングを適切に活用することで、より効率的で理解しやすいプログラムを作成することができます。