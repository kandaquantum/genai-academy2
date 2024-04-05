# GAS基礎プログラム実践

## 目次
- [GAS基礎プログラム実践とは](#introduction)
- [解説](#explanation)
  - [Hello world](#hello-world)
  - [メール一斉送信](#bulk-email)
  - [トリガーの使い方](#triggers)

<a id="introduction"></a>
## GAS基礎プログラム実践とは
Google Apps Script（GAS）は、Googleが提供するクラウドベースのスクリプト言語です。JavaScriptをベースとしており、Google WorkspaceのさまざまなサービスやAPIと連携することができます。GASを使用することで、Google Sheets、Google Docs、Gmailなどのアプリケーションを自動化し、効率的なワークフローを構築することができます。

本講義では、GASを用いた基礎的なプログラミングを実践的に学びます。メール一斉送信やトリガーの使い方など、実際のビジネスシーンで役立つスキルを身につけることができます。プログラミング初心者の方でも、わかりやすい解説と例題を通して、GASの基礎を習得することができます。

<a id="explanation"></a>
## 解説
GASを使用したプログラミングの詳細解説と簡単な例題を通して、実践的なスキルを身につけましょう。

もちろんです。GASの基礎的な使い方として、"Hello, World!"を出力する例題を追加しましょう。

<a id="hello-world"></a>

### Hello, World!の出力

#### 詳細解説

プログラミングを学ぶ際の最初のステップとして、"Hello, World!"を出力するプログラムを作成することが一般的です。GASでも同様に、簡単なスクリプトを作成し、実行結果を確認することができます。この例題を通して、GASの基本的な構文やデバッグ方法を学びましょう。

#### 例題と解説

以下は、GASで"Hello, World!"を出力するサンプルコードです。

```javascript
function helloWorld() {
  console.log("Hello, World!");
}
```

このコードでは、`helloWorld`という関数を定義しています。関数内では、`console.log`メソッドを使用して、"Hello, World!"という文字列をログ出力しています。

スクリプトエディタ上で`helloWorld`関数を選択し、実行ボタンをクリックすると、関数が実行されます。実行結果は、スクリプトエディタ下部の"ログ"タブに表示されます。

```
[20XX/XX/XX XX:XX:XX:XXX JST] Hello, World!
```

<a id="bulk-email"></a>
### メール一斉送信
#### 詳細解説
GASを使用すると、Gmailと連携してメールの一斉送信を自動化することができます。受信者のリストをGoogle Sheetsに用意し、GASのスクリプトを実行することで、個別にメールを送信する手間を省くことができます。また、メールの本文にはGoogle Sheetsのデータを差し込むことも可能です。

#### 例題と解説
以下は、Google Sheetsに記載された受信者リストを元に、メールを一斉送信するサンプルコードです。

```python
function sendBulkEmail() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var dataRange = sheet.getDataRange();
  var data = dataRange.getValues();

  for (var i = 1; i < data.length; i++) {
    var recipient = data[i][0];
    var subject = "サンプルメール";
    var body = "こんにちは、" + data[i][1] + "さん\n\nこれはサンプルメールです。";

    GmailApp.sendEmail(recipient, subject, body);
  }
}
```

このコードでは、Google Sheetsのアクティブシートからデータを取得し、1行目をヘッダーとして扱います。2行目以降のデータを順番に処理し、1列目の値を受信者のメールアドレス、2列目の値を受信者の名前として使用しています。メールの件名と本文は固定の内容ですが、本文には受信者の名前を差し込んでいます。

<a id="triggers"></a>
### トリガーの使い方
#### 詳細解説
GASのトリガー機能を使用すると、特定のイベントをきっかけにスクリプトを自動実行することができます。例えば、指定した時間にスクリプトを実行したり、Google Sheetsの内容が変更された際にスクリプトを実行したりすることができます。トリガーを設定することで、手動でスクリプトを実行する手間を省き、自動化されたワークフローを構築することができます。

#### 例題と解説
以下は、毎日午前9時にGoogle Sheetsのデータを元にメールを送信するサンプルコードです。

```python
function setDailyTrigger() {
  ScriptApp.newTrigger("sendDailyEmail")
    .timeBased()
    .atHour(9)
    .everyDays(1)
    .create();
}

function sendDailyEmail() {
  var sheet = SpreadsheetApp.getActiveSheet();
  var dataRange = sheet.getDataRange();
  var data = dataRange.getValues();

  for (var i = 1; i < data.length; i++) {
    var recipient = data[i][0];
    var subject = "日次レポート";
    var body = "こんにちは、" + data[i][1] + "さん\n\n本日の日次レポートを送信します。\n\n売上: " + data[i][2] + "円\n訪問者数: " + data[i][3] + "人";

    GmailApp.sendEmail(recipient, subject, body);
  }
}
```

`setDailyTrigger`関数では、`sendDailyEmail`関数を毎日午前9時に実行するようにトリガーを設定しています。`sendDailyEmail`関数は、Google Sheetsのデータを取得し、各行のデータを元にメールを送信します。メールの本文には、売上と訪問者数のデータを差し込んでいます。

トリガーを設定することで、毎日決まった時間にレポートメールを自動送信することができます。
