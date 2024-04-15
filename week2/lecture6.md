
# CursorからのGAS開発

<a id="table-of-contents"></a>
## 目次
- [CursorからのGAS開発とは](#introduction)
- [解説](#explanation)
  - [GAS プロジェクトの準備](#gas-project-setup)
  - [Clasp のインストールとセットアップ](#clasp-setup)
  - [GAS プロジェクトとの同期](#gas-sync)
  - [Claspで特定の関数を実行する方法](#clasp-run-function)
  - [GitHub リポジトリとの連携](#github-integration)

<a id="introduction"></a>
## CursorからのGAS開発とは

CursorからのGAS開発とは、Google Apps Script (GAS) プロジェクトをローカル環境で開発し、バージョン管理システム（GitHubなど）と連携させる手法です。この手法では、Claspというコマンドラインツールを使用して、GASプロジェクトとローカル環境の同期を行います。

従来のGAS開発では、Googleのオンラインエディタを使用していましたが、この手法ではローカル環境でお気に入りのエディタ（VSCodeなど）を使用できます。また、バージョン管理システムとの連携により、コードの変更履歴を追跡したり、共同作業を行ったりすることが容易になります。

CursorからのGAS開発の主なメリットは以下の通りです：

1. ローカル環境での開発により、お気に入りのエディタやツールを使用できる
2. バージョン管理システムとの連携により、コードの変更履歴を追跡できる
3. 共同作業がしやすくなる
4. ローカルでのテストや自動化タスクの実行が可能になる

この手法を習得することで、GAS開発の効率と品質を大幅に向上させることができます。

<a id="explanation"></a>
## 解説

<a id="gas-project-setup"></a>
### GAS プロジェクトの準備

#### 詳細解説
GAS プロジェクトの準備では、まずGASプロジェクトを作成または開きます。次に、スクリプトエディタでプロジェクトのプロパティを開き、スクリプトIDをコピーします。このスクリプトIDは、後でClaspの設定ファイルで使用します。

#### 例題と解説
1. GASプロジェクトを新規作成または既存のプロジェクトを開く
2. ファイル > プロジェクトのプロパティ に移動
3. スクリプトIDをコピーする

```
// スクリプトID例
1A2b3C4d5E6f7G8h9I0j1K2l3M4n5O6p7Q8r9S0t
```

<a id="clasp-setup"></a>
### Clasp のインストールとセットアップ

#### 詳細解説
Claspのインストールとセットアップでは、npmを使用してClaspをグローバルにインストールします。次に、`clasp login`コマンドを実行してGoogleアカウントにログインします。その後、GASプロジェクトを保存するディレクトリに移動し、`clasp create`コマンドを実行して新しいClaspプロジェクトを初期化します。最後に、".clasp.json"ファイルにスクリプトIDを設定します。

#### 例題と解説
1. ターミナルで以下のコマンドを実行してClaspをインストール
   ```
   npm install -g @google/clasp
   ```

2. Claspにログイン
   ```
   clasp login
   ```

3. GASプロジェクトを保存するディレクトリに移動し、Claspプロジェクトを初期化
   ```
   clasp create --type standalone --rootDir ./
   ```

4. ".clasp.json"ファイルを開き、"scriptId"フィールドにスクリプトIDを設定
   ```json
   {
     "scriptId": "1A2b3C4d5E6f7G8h9I0j1K2l3M4n5O6p7Q8r9S0t",
     "rootDir": "./"
   }
   ```

<a id="gas-sync"></a>
### GAS プロジェクトとの同期

#### 詳細解説
GASプロジェクトとの同期では、`clasp pull`コマンドを使用して、GASプロジェクトのコードをローカルにプルします。コードに変更を加えた後、`clasp push`コマンドを使用して、変更をGASにプッシュします。

#### 例題と解説
1. GASプロジェクトのコードをローカルにプル
   ```
   clasp pull
   ```

2. コードに変更を加える
   ```js
   function myFunction() {
     console.log("Hello, World!");
   }
   ```

3. 変更をGASにプッシュ
   ```
   clasp push
   ```

<a id="clasp-run-function"></a>
### Claspで特定の関数を実行する方法

#### 詳細解説
Claspを使用して、GASプロジェクト内の特定の関数を実行するには、`clasp run`コマンドを使用します。実行する関数名を指定することで、その関数を直接実行できます。これにより、デプロイせずにローカルで関数をテストしたり、定期的なタスクを自動化したりすることができます。

#### 例題と解説
1. 実行したい関数を定義する
   ```js
   function sendBulkEmails() {
     // 一括メール送信の処理
   }
   ```

2. `clasp run`コマンドで関数を実行
   ```
   clasp run sendBulkEmails
   ```

3. 実行結果がターミナルに表示される

<a id="github-integration"></a>
### GitHub リポジトリとの連携

#### 詳細解説
GitHubリポジトリとの連携では、まずGitHubでリポジトリを作成または既存のリポジトリを使用します。次に、ローカルのClaspプロジェクトをGitHubリポジトリにプッシュします。これにより、GASプロジェクトとGitHubリポジトリが連携され、バージョン管理や共同作業が可能になります。

#### 例題と解説
1. GitHubでリポジトリを作成または既存のリポジトリを使用
2. ローカルのClaspプロジェクトをGitHubリポジトリにプッシュ
   ```
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/user/repo.git
   git push -u origin master
   ```

これで、GASプロジェクトとGitHubリポジトリが連携されました。Claspを使用してローカルでコードを編集し、変更をGASにプッシュできます。また、GitHubを使用してバージョン管理や共同作業を行うことができます。

[目次に戻る](#table-of-contents)