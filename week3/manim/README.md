# Manim アニメーションサンプル

このディレクトリには、[Manim](https://www.manim.community/)を使用して作成したアニメーションのサンプルスクリプトが含まれています。

## 必要条件

- Python 3.7以上
- Manim Community v0.17.2以上

## インストール

1. Python 3.7以上がインストールされていることを確認してください。

2. 仮想環境を作成し、アクティベートします。

```bash
python -m venv venv
source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
```

3. Manimをインストールします。

```bash
pip install manim
```

## 使用方法

1. `scripts`ディレクトリ内の目的のPythonスクリプトを選択します。

2. 以下のコマンドを実行して、アニメーションをレンダリングします。

```bash
manim -pql <script_name>.py <scene_name>
```

- `-pql`オプションは、アニメーションをプレビューし、中品質(480p)でレンダリングします。
- `<script_name>`は、実行するPythonスクリプトのファイル名です。
- `<scene_name>`は、スクリプト内で定義されているシーンクラスの名前です。

例:

```bash
manim -pql moe.py MixtureOfExperts
```

3. レンダリングされたアニメーションがプレビューウィンドウに表示されます。

## スクリプト一覧

- `moe.py`: Mixture of Experts (MoE)のアニメーション

## リソース

- [Manim公式ドキュメント](https://docs.manim.community/)
- [Manimコミュニティ](https://www.manim.community/)
