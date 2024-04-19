from manim import *

class MixtureOfExperts(Scene):
    def construct(self):
        # タイトル
        title = Text("Mixture of Experts (MoE)").scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # 入力
        input_text = MathTex("Input \, x").scale(0.7)
        input_text.move_to(LEFT * 5)  # 左に調整しました👈
        input_text_explanation = Text("入力データx", font_size=24).next_to(input_text, DOWN)
        self.play(Write(input_text), Write(input_text_explanation))

        # エキスパート🌟
        experts = VGroup(
            Circle(radius=0.5, color=BLUE, fill_opacity=1).set_fill(BLUE, opacity=0.5),
            Circle(radius=0.5, color=GREEN, fill_opacity=1).set_fill(GREEN, opacity=0.5),
            Circle(radius=0.5, color=RED, fill_opacity=1).set_fill(RED, opacity=0.5),
        ).arrange(DOWN, buff=1)
        experts.next_to(input_text, RIGHT, buff=1.5)  # 左に調整しました👈
        expert_labels = VGroup(
            MathTex(r"f_1(x)"),
            MathTex(r"f_2(x)"),
            MathTex(r"f_3(x)"),
        ).scale(0.7).arrange(DOWN, buff=1)
        expert_labels.next_to(experts, RIGHT)
        expert_labels_explanation = Text(
            "エキスパートの出力関数", 
            font_size=24
        ).next_to(expert_labels, DOWN * 5).shift(LEFT * 1)  # もっと下げて、左にも調整しました👇👈

        self.play(
            *[FadeIn(expert, scale=0.5) for expert in experts],  # エフェクト追加✨
            *[Write(label) for label in expert_labels],
            Write(expert_labels_explanation)
        )
        # エキスパートに光のエフェクトを追加しました🌈

        # 入力からエキスパートへの矢印
        input_arrows = VGroup(
            Arrow(start=input_text.get_right(), end=experts[0].get_left(), buff=0.1),
            Arrow(start=input_text.get_right(), end=experts[1].get_left(), buff=0.1),
            Arrow(start=input_text.get_right(), end=experts[2].get_left(), buff=0.1),
        )
        # 矢印が来たタイミングで、ぴこんってなるエフェクトを追加🌟
        def pikon_effect(arrow, expert):
            self.play(GrowArrow(arrow))
            self.play(Flash(expert, color=YELLOW, flash_radius=0.5))
        
        for arrow, expert in zip(input_arrows, experts):
            pikon_effect(arrow, expert)

        # ゲーティング関数を円に変更しました🔵
        gating_function = Circle(radius=0.5, color=YELLOW, fill_opacity=1).set_fill(YELLOW, opacity=0.5)
        gating_function.next_to(experts, RIGHT, buff=1.5)  # 左に調整しました👈
        gating_label = MathTex(r"w(x)").scale(0.7).next_to(gating_function, UP)
        gating_label_explanation = Text(
            "ゲーティング関数の重み", 
            font_size=24
        ).next_to(gating_label, UP * 2).shift(RIGHT * 1)  # 思いっきり右上に移動し、改行しました🚀👆➡️

        # 入力からゲーティング関数への矢印を追加し、その後消す処理を追加🚀
        input_to_gating_arrow = Arrow(start=input_text.get_right(), end=gating_function.get_left(), buff=0.1, color=YELLOW)
        self.play(GrowArrow(input_to_gating_arrow))
        self.remove(input_to_gating_arrow)  # 矢印を消します🗑️

        self.play(FadeIn(gating_function), Write(gating_label), Write(gating_label_explanation))

        # エキスパートからゲーティング関数への矢印
        gating_arrows = VGroup(
            Arrow(start=experts[0].get_right(), end=gating_function.get_left(), buff=0.1),
            Arrow(start=experts[1].get_right(), end=gating_function.get_left(), buff=0.1),
            Arrow(start=experts[2].get_right(), end=gating_function.get_left(), buff=0.1),
        )
        # 矢印が来たタイミングで、ぴこんってなるエフェクトを追加しました🌟
        # f(x)を矢印が見えた瞬間に消すように変更しました🚀
        def pikon_effect_gating(arrow, expert_label):
            self.play(GrowArrow(arrow), FadeOut(expert_label))  # f(x)を矢印と一緒に消します🗑️✨
            self.play(Flash(gating_function, color=YELLOW, flash_radius=0.5))
        
        for arrow, expert_label in zip(gating_arrows, expert_labels):
            pikon_effect_gating(arrow, expert_label)

        # 出力
        output_text = MathTex(r"\sum_{i=1}^{n} w(x)_i f_i(x)").scale(0.7)
        output_text.next_to(gating_function, RIGHT, buff=1.5)  # 左に調整しました👈
        output_text_explanation = Text("最終的な出力", font_size=24).next_to(output_text, DOWN)
        output_arrow = Arrow(start=gating_function.get_right(), end=output_text.get_left(), buff=0.1)


        self.play(GrowArrow(output_arrow), Write(output_text), Write(output_text_explanation))

        self.wait(2)


        # 今までの図を消しますが、タイトルは残します🧹✨ 矢印もぴゅーんと消えますよ〜🚀✨
        # expertsの丸と矢印もちゃんと消えるように修正しました👌✨
        self.remove(input_text)
        self.remove(experts)
        self.remove(expert_labels)
        self.remove(gating_function)
        self.remove(gating_label)
        self.remove(gating_label_explanation)
        self.remove(input_to_gating_arrow)
        self.remove(gating_arrows)
        self.remove(output_text)
        self.remove(output_text_explanation)
        self.remove(output_arrow)
        self.remove(input_arrows)
        self.remove(*experts)
        self.remove(*input_arrows)
        self.remove(*gating_arrows)
        # 入力データとエキスパートの出力関数を消します🧹✨
        self.remove(input_text_explanation)
        self.remove(expert_labels_explanation)
        # すっきりしましたね！🌈✨


        input_text = Text("可愛い広告バナーを\nつくってほしい").scale(0.5)  # 大きさをさらに調整しました📏
        input_text.move_to(LEFT * 5)  # もっと右に余白を作るために、さらに左に移動しました👈🌟
        self.play(Write(input_text))

        # エキスパート
        experts = Group(
            ImageMobject("marketing_character.png").scale(0.2),  # もっと小さくしました📏👌
            ImageMobject("designer_character.png").scale(0.2),  # もっと小さくしました📏👌
            ImageMobject("writer_character.png").scale(0.2),  # もっと小さくしました📏👌
        ).arrange(DOWN, buff=0.25)  # 間隔もさらに調整しました📐
        experts.next_to(input_text, RIGHT, buff=1)  # 間隔を広げました📐👉
        expert_labels = VGroup(
            Text("マーケター", font_size=30).next_to(experts[0], RIGHT, buff=0.2),  # 文字の大きさを調整し、画像の隣に配置しました📏👥
            Text("デザイナー", font_size=30).next_to(experts[1], RIGHT, buff=0.2),  # 間隔を広げました📐👉
            Text("ライター", font_size=30).next_to(experts[2], RIGHT, buff=0.2),  # 間隔を広げました📐👉
        )  

        self.play(
            *[FadeIn(expert, scale=0.25) for expert in experts],  # エフェクトの大きさもさらに調整しました🌟
            *[Write(label) for label in expert_labels],
        )

        # 入力からエキスパートへの矢印
        input_arrows = VGroup(
            Arrow(start=input_text.get_right(), end=experts[0].get_left(), buff=0.1),  # 間隔を広げました📐👉
            Arrow(start=input_text.get_right(), end=experts[1].get_left(), buff=0.1),  # 間隔を広げました📐👉
            Arrow(start=input_text.get_right(), end=experts[2].get_left(), buff=0.1),  # 間隔を広げました📐👉
        )
        for arrow, expert in zip(input_arrows, experts):
            self.play(GrowArrow(arrow), Flash(expert, color=YELLOW, flash_radius=0.25))  # エフェクトの大きさもさらに調整しました🌟

        # ゲーティング関数（ディレクター）
        gating_function = ImageMobject("director_character.png").scale(0.25)  # 大きさをさらに調整しました📏
        gating_function.next_to(experts, RIGHT, buff=1)  # 間隔を広げました📐👉
        gating_label = Text("ディレクター").scale(0.5).next_to(gating_function, UP)  # 大きさをさらに調整しました📏

        self.play(FadeIn(gating_function), Write(gating_label))

        # エキスパートからゲーティング関数への矢印
        gating_arrows = VGroup(
            Arrow(start=experts[0].get_right(), end=gating_function.get_left(), buff=0.1),  # 間隔を広げました📐👉
            Arrow(start=experts[1].get_right(), end=gating_function.get_left(), buff=0.1),  # 間隔を広げました📐👉
            Arrow(start=experts[2].get_right(), end=gating_function.get_left(), buff=0.1),  # 間隔を広げました📐👉
        )
        for arrow, expert_label in zip(gating_arrows, expert_labels):
            self.play(GrowArrow(arrow), FadeOut(expert_label))
            self.play(Flash(gating_function, color=YELLOW, flash_radius=0.25))  # エフェクトの大きさもさらに調整しました🌟

        # 出力
        output_image = ImageMobject("cute_ad_banner.png").scale(0.5)  # 大きさをさらに調整しました📏
        output_image.next_to(gating_function, RIGHT, buff=1)  # 間隔を広げました📐👉
        output_text = Text("可愛い広告バナー").scale(0.5).next_to(output_image, DOWN)  # 大きさをさらに調整しました📏
        output_arrow = Arrow(start=gating_function.get_right(), end=output_image.get_left(), buff=0.1)  # 間隔を広げました📐👉

        self.play(GrowArrow(output_arrow), FadeIn(output_image), Write(output_text))

        self.wait(2)