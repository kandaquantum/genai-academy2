# 生成AI概論

スライドURL: https://www.canva.com/design/DAF-Ts96_CY/M6fq49rcZ7JX815XLb_xDQ/view?utm_content=DAF-Ts96_CY&utm_campaign=designshare&utm_medium=link&utm_source=editor

## 目次
- [AIの歴史](#ai-history)
- [3大基盤モデル](#three-foundation-models)
- [3大AIモデル](#three-ai-models)
- [統合モデル（LMM、MLLM）](#integrated-models)
- [マルチモーダル = マルチな情報源](#multimodal-multi-source)
- [マルチモーダルAI 一連の流れ](#multimodal-ai-flow)
- [RAGの仕組み](#rag-mechanism)
- [GoogleGemini](#google-gemini)
- [OpenAI Sora](#openai-sora)
- [アリババ EMO: Emote Portrait Alive](#alibaba-emo)

<a id="ai-history"></a>
## AIの歴史
AIの歴史は1960年代に始まり、1980年代の2次ブームののち「AIの冬の時代」と呼ばれる停滞期がありましたが、2010年代以降第三次生成AIブームが始まり、Attention、Transformer（2017年）、Diffusion Model（2015年）などの登場により、再び発展期を迎えています。2012年にはAlphaGoが登場し、AIが人間を上回る性能を示しました。2022年にはChatGPT（2022年12月）とMidjourney（2022年7月）が登場し、AI技術が一般にも広く知られるようになりました。

<a id="three-foundation-models"></a>
## 3大基盤モデル
AI技術の発展を支える3つの大規模モデルがあります。

1. 大規模言語モデル（Large Language Model、LLM）: 「計算量」「データ量」「パラメータ数」を大幅に増やした言語モデル
2. 視覚言語モデル（Vision Language Model、VLM）: LLMに視覚モデルを付随させたモデル
3. 大規模視覚モデル（Large Vision Model、LVM）: 大規模な視覚情報のみで学習させたモデル

<a id="three-ai-models"></a>
## 3大AIモデル
AI技術の中で特に重要な3つのモデルを紹介します。

1. トランスフォーマーモデル: 自己注意機構を使用してテキストの文脈を理解し、自然言語処理タスクに革命をもたらしたAI技術
2. Diffusionモデル: 逐次的なノイズの除去プロセスを通じて高品質な画像を生成する、深層学習に基づく画像生成技術
3. DiT: Diffusionモデルとトランスフォーマーモデルを合わせたモデルで、OpenAIのSoraなどに利用されている

<a id="integrated-models"></a>
## マルチモーダルモデル（LMM、MLLM）
マルチモーダルモデルは、言語、視覚、音声などのマルチモーダルな情報を統合して処理できるモデルです。LMM（Large Multimodal Model）やMLLM（Multimodal Large Language Model）と呼ばれることもあります。これらのモデルは、より自然で人間に近いインタラクションを可能にすると期待されています。

<a id="multimodal-multi-source"></a>
## マルチモーダル = マルチな情報源
マルチモーダルとは、視覚、聴覚、など五感の情報+テキストの複数の情報源を融合して処理することを指します。これにより、より豊かで正確な情報理解が可能になります。

<a id="multimodal-ai-flow"></a>
## マルチモーダルAI 一連の流れ
マルチモーダルAIの一連の流れは以下のようになります。

1. 五感情報の取り込み（Input）:
- 視覚情報の取り込み 
    - 画像やビデオなどの視覚情報をテキストに変換
    - 人間の目に相当する機能で、外界の情報を取り込む
- 聴覚情報の取り込み
    - 音声や音楽などの聴覚情報をテキストに変換  
    - 人間の耳に相当する機能で、外界の情報を取り込む

2. テキスト情報の処理（Memory & Thinking）:
   - 視覚情報から変換されたテキストや元からあるテキストを処理
   - 取り込んだ情報を記憶し、それを基に思考を行う

3. 出力情報の解釈と生成（Output）:
   - 処理されたテキスト情報を画像、ビデオ、モーション、3Dモデル、仮想世界などに変換
   - 思考の結果を外界に表現する

4. 応用例:
   - AIが生成したニュース、映画、アニメーションなど
   - 取り込んだ情報を基に生成されたクリエイティブなアウトプット

<a id="rag-mechanism"></a>
## RAGの仕組み
RAG（Retrieval-Augmented Generation）は、大規模言語モデルの生成能力を向上させる手法です。RAGは以下の2つの要素で構成されます。

1. 短期記憶: 大規模言語モデルのトークン
2. 外付け記憶: ベクトルデータベース

RAGは、外付け記憶から関連する情報を取得し、短期記憶と組み合わせることで、より正確で詳細な応答を生成できます。


<a id="google-gemini"></a>
## GoogleGemini
GoogleGeminiは、Googleが開発しているマルチモーダルAIの一例です。動画、画像、テキストなどの複数の情報源を統合して処理することで、より自然で正確な応答を生成できます。

<a id="openai-sora"></a>
## OpenAI Sora
OpenAI Soraは、OpenAIが開発している動画生成AIの一例です。Soraは、Diffusionモデルとトランスフォーマーモデルを組み合わせたDiTモデルを使用していると言われており、高品質な動画生成と自然言語処理を実現しています。
