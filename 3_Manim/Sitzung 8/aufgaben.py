from manim import *

class ProductRuleAnimation(Scene):
    def construct(self):
        # Schritt 1: Ursprungsformel
        start = MathTex(r"{{\frac{d}{dx}}} \left[ {{f(x)}} \cdot {{g(x)}} \right]", font_size=72).shift(UP)
        self.play(Write(start))
        self.add(index_labels(start))
        self.wait()
        print(len(start))

        # Schritt 2: Produktregel
        result = MathTex(
            r"{{\frac{d}{dx}}} {{f(x)}} \cdot {{g(x)}} + {{f(x)}} \cdot {{\frac{d}{dx}}}{{g(x)}}",
            font_size=72
        ).shift(DOWN)
        self.add(index_labels(result))

        self.play(
            TransformFromCopy(start[0], result[0]),
            TransformFromCopy(start[2], result[2]),
        )
        self.play(FadeIn(result[3]))
        self.play(TransformFromCopy(start[4], result[4]))
        self.play(FadeIn(result[5]))
        self.play(TransformFromCopy(start[2], result[6]))
        self.play(FadeIn(result[7]))
        self.play(TransformFromCopy(start[0], result[8]), TransformFromCopy(start[4], result[10]))
        self.wait()


