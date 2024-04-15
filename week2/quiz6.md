# 問題集

<a id="introduction"></a>

## はじめに

この講義では、CursorからGASを使ってメーリングリストへの一斉送信を行い、書籍を売り込む方法について学びます。GASとClaspを連携させ、GitHubリポジトリを活用した開発手順を理解することを目的としています。

<a id="quiz"></a>

## 4択問題

<details>
<summary>問題1: GASプロジェクトのスクリプトIDを確認するには、どこを見ればよいでしょうか？</summary>

- a. ファイル > プロジェクトを開く
- b. ファイル > プロジェクトのプロパティ
- c. 編集 > 現在のプロジェクトのプロパティ 
- d. ツール > スクリプトID

<details>
<summary>回答と解説</summary>

回答: b. ファイル > プロジェクトのプロパティ

GASプロジェクトのスクリプトIDは、スクリプトエディタで「ファイル」メニューの「プロジェクトのプロパティ」から確認できます。スクリプトIDは、Claspを使ってGASプロジェクトと連携する際に必要となります。
</details>
</details>

<details>
<summary>問題2: Claspをグローバルにインストールするためのコマンドは？</summary>

- a. npm install -g clasp
- b. npm install -g @google/clasp
- c. npm install -g gas-clasp
- d. npm install -g google-clasp

<details>
<summary>回答と解説</summary>

回答: b. npm install -g @google/clasp

Claspをグローバルにインストールするには、`npm install -g @google/clasp`コマンドを使用します。`@google/clasp`はClaspのパッケージ名であり、`-g`オプションはグローバルインストールを指定しています。
</details>
</details>

<details>
<summary>問題3: GASプロジェクトのコードをローカルにプルするためのClaspコマンドは？</summary>

- a. clasp push
- b. clasp pull
- c. clasp sync
- d. clasp clone

<details>
<summary>回答と解説</summary>

回答: b. clasp pull

GASプロジェクトのコードをローカルにプルするには、`clasp pull`コマンドを使用します。このコマンドにより、GASプロジェクトのコードがローカルのディレクトリにダウンロードされ、ローカルで編集できるようになります。
</details>
</details>

<details>
<summary>問題4: Claspを使って特定の関数を実行するコマンドは？</summary>

- a. clasp run
- b. clasp execute
- c. clasp call
- d. clasp function

<details>
<summary>回答と解説</summary>

回答: a. clasp run

Claspを使って特定の関数を実行するには、`clasp run`コマンドを使用します。`clasp run <関数名>`のように、実行したい関数名を指定することで、GASプロジェクト内の特定の関数を直接実行できます。
</details>
</details>

<details>
<summary>問題5: Claspを使ってGASプロジェクトをGitHubリポジトリと連携するために必要なファイルは？</summary>

- a. .clasp.json
- b. .clasprc.json
- c. .clasp.config
- d. .clasp.js

<details>
<summary>回答と解説</summary>

回答: a. .clasp.json

GASプロジェクトをGitHubリポジトリと連携するには、`.clasp.json`ファイルが必要です。このファイルには、GASプロジェクトのスクリプトIDなどの設定情報が記述されています。`.clasp.json`ファイルをGitHubリポジトリにプッシュすることで、GASプロジェクトとGitHubリポジトリが連携されます。
</details>
</details>

この講義を通じて、CursorからGASを使ってメーリングリストへの一斉送信を行う方法と、ClaspとGitHubリポジトリを活用したGAS開発の手順について理解を深めることができます。実際にコードを書いて試してみることで、より実践的なスキルが身につくでしょう。