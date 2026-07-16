from manim import *


class GPUAnimationTest(Scene):
    def construct(self):
        square = Square(color=BLUE).scale(1.5)
        circle = Circle(color=PURPLE).scale(1.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(square.animate.rotate(PI / 4).shift(UP * 0.5))
        self.wait(1)
