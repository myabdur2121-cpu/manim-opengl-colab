from manim import *


class Formula(Scene):
    def construct(self):
        eq = MathTex(r"\int_{0}^{\infty} e^{-x^2}\,dx = \frac{\sqrt{\pi}}{2}")
        eq.scale(1.4)
        title = Text("Gaussian integral", font_size=36).next_to(eq, UP, buff=0.6)

        self.play(Write(title))
        self.play(Write(eq))
        self.wait(2)
