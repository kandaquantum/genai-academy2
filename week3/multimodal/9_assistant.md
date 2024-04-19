
# 目次
## OpenAI アシスタントAPI入門

1. [事前準備](#事前準備)
   - [OpenAIのアカウント登録とAPIキーの取得](#openaiapiキーの取得)
   - [Python 3.7以上のインストール](#python-37以上のインストール)
   - [OpenAI Python SDKのインストール](#openai-python-sdkのインストール)
2. [ステップ1: アシスタントの作成](#ステップ1-アシスタントの作成)
3. [ステップ2: スレッドの作成](#ステップ2-スレッドの作成)
4. [ステップ3: メッセージの追加](#ステップ3-メッセージの追加)
5. [ステップ4: 実行とストリーミング](#ステップ4-実行とストリーミング)
   - [EventHandlerクラスの定義](#eventhandlerクラスの定義)
   - [stream.until_done()の使用](#streamuntil_doneの使用)

## OpenAI File Search入門

2. [ステップ1: File Searchを有効にしたアシスタントの作成](#ステップ1-file-searchを有効にしたアシスタントの作成)
3. [ステップ2: ファイルのアップロードとVector Storeの作成](#ステップ2-ファイルのアップロードとvector-storeの作成)
4. [ステップ3: アシスタントにVector Storeを関連付ける](#ステップ3-アシスタントにvector-storeを関連付ける)
5. [ステップ4: スレッドの作成とファイルの添付](#ステップ4-スレッドの作成とファイルの添付)
6. [ステップ5: 実行とレスポンスの確認](#ステップ5-実行とレスポンスの確認)
7. [File Searchの仕組み](#file-searchの仕組み)
8. [Vector Storeの管理](#vector-storeの管理)

## OpenAI アシスタントAPI v2の新機能


# OpenAI アシスタントAPI入門

OpenAIのアシスタントAPIを使うと、独自のAIアシスタントをアプリケーションに組み込むことができます。このガイドでは、Python SDKを使ってアシスタントAPIの基本的な使い方を学びます。

## 事前準備

- OpenAIのアカウント登録とAPIキーの取得
- Python 3.7以上のインストール
- OpenAI Python SDKのインストール (`pip install openai`)

## ステップ1: アシスタントの作成

最初に、アシスタントのインスタンスを作成します。この際、モデルの種類や初期命令、利用可能なツールなどを指定します。

```python
from openai import OpenAI

client = OpenAI()

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-turbo",
)
```

## ステップ2: スレッドの作成

ユーザーとアシスタントのやり取りは、スレッドという単位で管理されます。新しい会話を始める際は、スレッドを作成します。

```python
thread = client.beta.threads.create()
```

## ステップ3: メッセージの追加

ユーザーのメッセージをスレッドに追加します。メッセージにはテキストやファイルを含められます。

```python
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)
```

## ステップ4: 実行とストリーミング

メッセージの追加が完了したら、アシスタントを実行してレスポンスを生成します。`stream`ヘルパーを使うと、リアルタイムでレスポンスを受信できます。

```python
from typing_extensions import override
from openai import AssistantEventHandler

class EventHandler(AssistantEventHandler):    
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)
        
    @override
    def on_text_delta(self, delta, snapshot):
        print(delta.value, end="", flush=True)
        
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)
    
    def on_tool_call_delta(self, delta, snapshot):
        if delta.type == 'code_interpreter':
            if delta.code_interpreter.input:
                print(delta.code_interpreter.input, end="", flush=True)
            if delta.code_interpreter.outputs:
                print(f"\n\noutput >", flush=True)
                for output in delta.code_interpreter.outputs:
                    if output.type == "logs":
                        print(f"\n{output.logs}", flush=True)

with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
    event_handler=EventHandler(),
) as stream:
    stream.until_done()
```

`EventHandler`クラスを定義することで、レスポンスの各部分に対する処理を記述できます。上記の例では、テキストやツールの呼び出し、コード実行結果などをリアルタイムで出力しています。

以上が、アシスタントAPIを使ったシンプルなPythonプログラムの例です。この基本的な流れを応用することで、様々なユースケースに対応したAIアシスタントを開発できるでしょう。

# OpenAI File Search入門

OpenAIのFile Searchツールを使うと、独自のデータでアシスタントの知識ベースを拡張できます。このガイドでは、File Searchを使ってファイルをアシスタントに読み込ませる方法を学びます。

## 事前準備

- OpenAIのアカウント登録とAPIキーの取得
- Python 3.7以上のインストール
- OpenAI Python SDKのインストール (`pip install openai`)

## ステップ1: File Searchを有効にしたアシスタントの作成

まず、`file_search`ツールを有効にしたアシスタントを作成します。

```python
from openai import OpenAI

client = OpenAI()

assistant = client.beta.assistants.create(
    name="Financial Analyst Assistant",
    instructions="You are an expert financial analyst. Use you knowledge base to answer questions about audited financial statements.",
    model="gpt-4-turbo",
    tools=[{"type": "file_search"}],
)
```

## ステップ2: ファイルのアップロードとVector Storeの作成

File Searchで使うファイルは、Vector Storeというオブジェクトで管理します。Vector Storeを作成し、そこにファイルをアップロードします。

```python
# Create a vector store called "Financial Statements"
vector_store = client.beta.vector_stores.create(name="Financial Statements")

# Ready the files for upload to OpenAI 
file_paths = ["edgar/goog-10k.pdf", "edgar/brka-10k.txt"]
file_streams = [open(path, "rb") for path in file_paths]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

print(file_batch.status)
print(file_batch.file_counts)
```

## ステップ3: アシスタントにVector Storeを関連付ける 

アップロードしたファイルをアシスタントから利用できるようにするには、`tool_resources`パラメータでVector Store IDを指定します。

```python
assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)
```

## ステップ4: スレッドの作成とファイルの添付

アシスタントとのやり取りはスレッド単位で管理されます。スレッドを作成する際、ファイルを添付することもできます。添付されたファイルは、そのスレッド専用のVector Storeに格納されます。

```python
# Upload the user provided file to OpenAI
message_file = client.files.create(
    file=open("edgar/aapl-10k.pdf", "rb"), purpose="assistants"
)

# Create a thread and attach the file to the message
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user", 
            "content": "How many shares of AAPL were outstanding at the end of of October 2023?",
            # Attach the new file to the message.
            "attachments": [
                { "file_id": message_file.id, "tools": [{"type": "file_search"}] }
            ],
        }
    ]
)

print(thread.tool_resources.file_search)
```

## ステップ5: 実行とレスポンスの確認

最後に、`runs.stream`メソッドでFile Searchを実行し、アシスタントのレスポンスを確認します。

```python
from typing_extensions import override
from openai import AssistantEventHandler

class EventHandler(AssistantEventHandler):
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)

    @override
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    @override
    def on_message_done(self, message) -> None:
        message_content = message.content[0].text
        annotations = message_content.annotations
        citations = []
        for index, annotation in enumerate(annotations):
            message_content.value = message_content.value.replace(
                annotation.text, f"[{index}]"
            )
            if file_citation := getattr(annotation, "file_citation", None):
                cited_file = client.files.retrieve(file_citation.file_id)
                citations.append(f"[{index}] {cited_file.filename}")

        print(message_content.value)
        print("\n".join(citations))

with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Jane Doe. The user has a premium account.",
    event_handler=EventHandler(),
) as stream:
    stream.until_done()
```

上記の例では、アシスタントは2つのVector Store（googとbrkaの10-Kファイルを含むもの、aaplの10-Kファイルを含むもの）を検索し、aaplの10-Kファイルから該当する情報を引用してレスポンスを生成します。

## File Searchの仕組み

File Searchは、以下のような最適化によって適切な情報をファイルから抽出します。

- ユーザークエリの書き換えによる検索の最適化
- 複雑なクエリの分割と並列検索
- アシスタントとスレッドの両方のVector Storeに対するキーワード検索と意味検索
- 最終レスポンス生成前の検索結果の再ランク付け

## Vector Storeの管理

Vector Storeの使用量に応じて料金が発生します。コスト管理のため、Vector Storeにはファイルの有効期限ポリシーを設定できます。特にスレッド単位で作成されるVector Storeには、デフォルトで7日間のアクティブでない期間後に削除されるポリシーが適用されます。

以上がFile Searchの基本的な使い方です。大量のファイルをアシスタントに読み込ませ、ユーザーの質問に対して適切な情報を引用しながら回答できるようになります。



# OpenAI File Search入門

OpenAIのFile Searchツールを使うと、独自のデータでアシスタントの知識ベースを拡張できます。このガイドでは、File Searchを使ってファイルをアシスタントに読み込ませる方法を学びます。

## 事前準備

- OpenAIのアカウント登録とAPIキーの取得
- Python 3.7以上のインストール
- OpenAI Python SDKのインストール (`pip install openai`)

## ステップ1: File Searchを有効にしたアシスタントの作成

まず、`file_search`ツールを有効にしたアシスタントを作成します。

```python
from openai import OpenAI

client = OpenAI()

assistant = client.beta.assistants.create(
    name="Financial Analyst Assistant",
    instructions="You are an expert financial analyst. Use you knowledge base to answer questions about audited financial statements.",
    model="gpt-4-turbo", 
    tools=[{"type": "file_search"}],
)
```

## ステップ2: ファイルのアップロードとVector Storeの作成

File Searchで使うファイルは、Vector Storeというオブジェクトで管理します。Vector Storeを作成し、そこにファイルをアップロードします。

```python
# Create a vector store called "Financial Statements"
vector_store = client.beta.vector_stores.create(name="Financial Statements")

# Ready the files for upload to OpenAI
file_paths = ["edgar/goog-10k.pdf", "edgar/brka-10k.txt"] 
file_streams = [open(path, "rb") for path in file_paths]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id, files=file_streams
)

print(file_batch.status)
print(file_batch.file_counts)
```

## ステップ3: アシスタントにVector Storeを関連付ける

アップロードしたファイルをアシスタントから利用できるようにするには、`tool_resources`パラメータでVector Store IDを指定します。

```python
assistant = client.beta.assistants.update(
    assistant_id=assistant.id,
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)
```

## ステップ4: スレッドの作成とファイルの添付

アシスタントとのやり取りはスレッド単位で管理されます。スレッドを作成する際、ファイルを添付することもできます。添付されたファイルは、そのスレッド専用のVector Storeに格納されます。 

```python
# Upload the user provided file to OpenAI
message_file = client.files.create(
    file=open("edgar/aapl-10k.pdf", "rb"), purpose="assistants"
)

# Create a thread and attach the file to the message
thread = client.beta.threads.create(
    messages=[
        {
            "role": "user",
            "content": "How many shares of AAPL were outstanding at the end of of October 2023?",
            # Attach the new file to the message.
            "attachments": [
                { "file_id": message_file.id, "tools": [{"type": "file_search"}] }
            ],
        }
    ]
)

print(thread.tool_resources.file_search)
```

## ステップ5: 実行とレスポンスの確認

最後に、`runs.stream`メソッドでFile Searchを実行し、アシスタントのレスポンスを確認します。

```python
from typing_extensions import override  
from openai import AssistantEventHandler

class EventHandler(AssistantEventHandler):
    @override
    def on_text_created(self, text) -> None:
        print(f"\nassistant > ", end="", flush=True)

    @override  
    def on_tool_call_created(self, tool_call):
        print(f"\nassistant > {tool_call.type}\n", flush=True)

    @override
    def on_message_done(self, message) -> None:
        message_content = message.content[0].text
        annotations = message_content.annotations
        citations = []
        for index, annotation in enumerate(annotations):
            message_content.value = message_content.value.replace(
                annotation.text, f"[{index}]"
            )
            if file_citation := getattr(annotation, "file_citation", None):
                cited_file = client.files.retrieve(file_citation.file_id)
                citations.append(f"[{index}] {cited_file.filename}")

        print(message_content.value)
        print("\n".join(citations))

with client.beta.threads.runs.stream(
    thread_id=thread.id,
    assistant_id=assistant.id,  
    instructions="Please address the user as Jane Doe. The user has a premium account.",
    event_handler=EventHandler(),
) as stream:
    stream.until_done()
```

上記の例では、アシスタントは2つのVector Store（googとbrkaの10-Kファイルを含むもの、aaplの10-Kファイルを含むもの）を検索し、aaplの10-Kファイルから該当する情報を引用してレスポンスを生成します。

## File Searchの仕組み

File Searchは、以下のような最適化によって適切な情報をファイルから抽出します。

- ユーザークエリの書き換えによる検索の最適化
- 複雑なクエリの分割と並列検索  
- アシスタントとスレッドの両方のVector Storeに対するキーワード検索と意味検索
- 最終レスポンス生成前の検索結果の再ランク付け

デフォルトでは、以下の設定が使用されます。

- チャンクサイズ: 800トークン
- チャンクオーバーラップ: 400トークン
- 埋め込みモデル: text-embedding-3-large (256次元)
- コンテキストに追加されるチャンクの最大数: 20 (状況によって少なくなる場合あり)

## Vector Storeの管理

Vector Storeの使用量に応じて料金が発生します。コスト管理のため、Vector Storeにはファイルの有効期限ポリシーを設定できます。特にスレッド単位で作成されるVector Storeには、デフォルトで7日間のアクティブでない期間後に削除されるポリシーが適用されます。 

```python
vector_store = client.beta.vector_stores.create_and_poll( 
    name="Product Documentation",
    file_ids=['file_1', 'file_2', 'file_3', 'file_4', 'file_5'], 
    expires_after={
        "anchor": "last_active_at",
        "days": 7
    }
)
```

Vector Storeの有効期限が切れると、そのスレッドでの実行が失敗します。これを修正するには、同じファイルで新しいVector Storeを作成し、スレッドに再度アタッチします。

```python
all_files = list(client.beta.vector_stores.files.list("vs_expired"))

vector_store = client.beta.vector_stores.create(name="rag-store") 
client.beta.threads.update(
    "thread_abc123",
    tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},  
)

for file_batch in chunked(all_files, 100):
    client.beta.vector_stores.file_batches.create_and_poll(
        vector_store_id=vector_store.id, file_ids=[file.id for file in file_batch]
    )
```

以上がFile Searchの基本的な使い方です。大量のファイルをアシスタントに読み込ませ、ユーザーの質問に対して適切な情報を引用しながら回答できるようになります。


# OpenAI アシスタントAPI v2の新機能

OpenAIは2024年4月、アシスタントAPIの新バージョンであるv2をベータリリースしました。以下は、v2で導入された主な新機能と改善点です。



| 機能 | 概要 | ビジネス視点での解説 |
|------|------|------------------|
| file_searchの強化 | アシスタントあたり最大10,000個のファイル取り込み可能、高速化と並列クエリ、再ランキングとクエリ書き換え機能強化 | 大量のファイルを効率的に処理できるようになり、情報検索の精度と速度が向上。ビジネスに関連する膨大なドキュメントをAIに読み込ませ、迅速に必要な情報を見つけ出せる。 |
| vector_storeオブジェクトの導入 | ファイルを自動的に解析、チャンク化、ベクトル化し検索可能に。アシスタントやスレッド全体で共有可能で、ファイル管理と請求が簡素化。 | ファイルの管理が容易になり、複数のアシスタントやスレッドで知識を共有できる。これにより、一貫性のある回答を生成でき、ファイルの管理コストも削減できる。 |
| 実行時のトークン使用量の制御 | 実行あたりのトークン使用量の上限設定が可能。実行で参照する過去のメッセージ数の制限設定も可能。 | APIの使用コストを最適化でき、予算管理がしやすくなる。不要に長い会話履歴を参照させないことで、効率的な処理が可能。 |
| tool_choiceパラメータのサポート | file_search, code_interpreter, functionなどの特定ツールの使用を強制可能。 | タスクに応じて最適なツールを選択でき、AIの能力を最大限に引き出せる。専門的な処理を必要とする場面で威力を発揮。 |
| カスタム会話履歴の作成 | assistantロールを使ったメッセージ作成で、スレッド内にカスタム履歴を生成可能。 | ユースケースに合わせた会話の流れを設計でき、AIとのインタラクションを最適化。ビジネスシーンに特化した会話モデルの構築が可能。 |
| 一般的なモデル設定パラメータのサポート | temperature, response_format(JSONモード), top_pなどが指定可能に。 | AIの出力をコントロールでき、ビジネス要件に合わせて調整可能。JSON形式での出力により、システムとの連携が容易に。 |
| 微調整モデルのサポート | 現在はgpt-3.5-turbo-0125の微調整版のみサポート。 | 自社データを用いてAIを微調整でき、ビジネスに特化した知識を持つAIの創出が可能。機密情報を扱う際にも安心。 |
| ストリーミングのサポート | リアルタイムでAIの出力を取得可能。 | ユーザーの問いかけに即座に反応でき、インタラクティブな体験の提供が可能。チャットボットなどに活用できる。 |
| Node.js, Python SDKの強化 | ストリーミング・ポーリングヘルパーを追加。 | 開発者の利便性が向上し、AIを簡単にアプリケーションに組み込める。社内の開発リソースを有効活用できる。 |