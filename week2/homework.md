# 初級課題

## 課題1: GPTsを使った初級チャットボット作成

### 目的
GPTsを使用して、オリジナルのチャットボットを作成します。

### 要件
- GPTsでチャットボットを作成してください。
- チャットボットの概要をAIと相談して決めてください。
  - タイトル
  - ロゴ
  - 役割や目標
  - 気をつけるべき点
  - 会話のトーン
- ユーザーが「終了」と入力するまで、チャットボットとの会話を続けるようにしてください。

### ヒント
- GPTsの使い方は、講義資料や公式ドキュメントを参照してください。
- AIと対話しながら、ユニークで魅力的なチャットボットを作成しましょう。
  - 例: 面白いキャラ設定、独自の言い回し、豊かな知識など

### 提出方法
- 作成したチャットボットのConfigure画面を、Google Docsに格納してください。
- Google Docsのファイルを、指定されたGoogle Driveのフォルダにアップロードしてください。
- 提出期限は、4/20土曜の9時までです。

この課題を通じて、GPTsを使った簡単なチャットボット作成の基本を学び、AIを活用したアプリケーション開発の第一歩を踏み出しましょう。



# 中級課題
## 課題1: Claudeを使ったカスタマイズ可能なテキスト生成

### 目的
Claudeを使用して、特定のトピックに基づいた記事を生成するプログラムを作成します。

### 要件
- Pythonを使用してプログラムを作成してください。
- AnthropicのClaude APIを利用して、指定されたトピックに基づいた記事を生成します。
- ユーザーがトピックを入力できるようにし、そのトピックに基づいた記事を生成してください。

### ヒント
- Anthropicの公式ドキュメントを参照して、APIの使い方を確認してください。
- トピックは、ユーザーが自由に入力できるようにしてください。

## 提出方法
- 作成したプログラムのソースコードを指定されたGoogle Driveのフォルダにアップロードしてください。
- 提出期限は、4/20土曜の9時までです。

## 課題2: GPT-4を使ったキャラクターボット

### 目的
GPT-4を使用して、自分の好きなキャラクターや人物になりきって会話するチャットボットを作成します。

### 要件
- Pythonを使用してプログラムを作成してください。
- OpenAIのGPT-4 APIを利用して、指定したキャラクターや人物のような回答を生成します。
- ユーザーが「終了」と入力するまで、キャラクターや人物になりきって会話を続けるようにしてください。
- キャラクターや人物の性格や口調を事前にGPT-4に伝え、それに沿った回答を生成するようにしてください。

### ヒント
- OpenAIの公式ドキュメントを参照して、APIの使い方を確認してください。
    - https://platform.openai.com/docs/quickstart?context=python
- `input()`関数を使用して、ユーザーからの入力を受け取ることができます。



### 提出方法
- 作成したプログラムのソースコードを、指定された提出フォームにアップロードしてください。 
- 提出期限は、4/20土曜の9時までです。



## 課題4: 講義資料自動生成プログラムを使った書籍作成

### 目的
GitHubにある講義資料自動生成プログラムを使って、自分オリジナルの書籍を作成し、Google Driveに保存します。

### 要件

利用するURL
https://github.com/kandaquantum/lecture_generator



| 手順 | 説明 | 小学生向けの説明 |
|------|------|----------------|
| 1. README.mdを読み、プログラムの使い方を理解する | プログラムの使用方法や必要な環境設定などが記載されたドキュメントを確認します。これにより、プログラムを正しく実行するための知識が得られます。 | プログラムの説明書を読むことで、そのプログラムの使い方がわかるようになるんだよ。ちょうど、新しいおもちゃの遊び方を説明書で確認するみたいだね。 |
| 2. 指定されたリポジトリをgit clone（ダウンロード）する | プログラムのソースコードをローカル環境にダウンロードします。これにより、プログラムを実行するために必要なファイルが手元に揃います。 | お友達からプログラムを借りるようなものだよ。これで、自分のパソコンでそのプログラムを使えるようになるんだ。 |
| 3. プログラムを使って、自分オリジナルの書籍を作成する | ダウンロードしたプログラムを実行し、自分独自の内容で書籍を作成します。プログラムが自動的に書籍の構成を生成してくれるので、効率的に作業を進められます。 | 借りてきたプログラムを使って、自分だけの本を作るんだよ。プログラムが本の骨組みを作ってくれるから、とっても簡単に本が作れちゃうんだ。 |
| 4. 作成した書籍をCursorを用いて修正変更する | 生成された書籍の内容を、Cursorを使って複数回修正・変更します。これにより、自分の意図に沿った内容に仕上げることができます。 | 作った本の内容を、Cursorというツールを使って何度も直していくんだよ。これで、自分のイメージ通りの本に仕上げることができるんだ。 |
| 5. Open Interpreterを利用して、ステージング環境に置くファイルを選択（add）する | Open Interpreterを開き、ステージング環境に追加するファイルを選択します。これにより、変更内容を管理下に置くことができます。 | Open Interpreterを使って、変更したファイルを「ステージ」に置くんだよ。これは、変更したファイルを管理するための特別な場所みたいなものなんだ。 |
| 6. Open Interpreterを利用して、ファイルを保存（commit）する | 選択したファイルの変更内容を、Open Interpreterを使ってcommitします。これにより、変更内容が記録され、後から参照できるようになります。 | 「ステージ」に置いたファイルを、Open Interpreterを使って「コミット」するんだよ。これは、変更内容を記録することで、後で見返せるようにするためなんだ。 |
| 7. Open Interpreterを利用して、ファイルをアップロード（push）する | commitした変更内容を、Open Interpreterを使ってリモートリポジトリにpushします。これにより、変更内容が他の人と共有されます。 | 記録した変更内容を、Open Interpreterを使ってインターネット上の保管場所に「プッシュ」するんだよ。これで、他の人とも変更内容を共有できるようになるんだ。 |
| 8. 自分のGitHubリポジトリのURLを提出する | 作成した書籍がアップロードされているGitHubリポジトリのURLを提出します。これにより、課題の完了を確認してもらえます。 | 作った本がアップロードされているインターネット上の場所のアドレスを先生に教えるんだよ。これで、宿題が完成したことを先生に伝えられるんだ。 |
### ヒント
- git cloneコマンドを使って、リポジトリをローカル環境にダウンロードしてください。
- README.mdには、プログラムの使い方や必要な環境設定などが記載されています。
- プログラムを実行する際は、適切な引数を指定してください。

### 提出方法
- 作成した書籍のPDFファイルを、指定されたGoogle Driveにアップロードしてください。
- 提出期限は、4/20土曜の9時までです。

この課題を通じて、既存のプログラムを活用して効率的に書籍を作成する方法を学びましょう。プログラムの使い方を理解し、自分なりの工夫を加えて、オリジナリティのある書籍を作成してください。