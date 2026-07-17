from manim import *


class Demo(Scene):
    def construct(self):
        s = Square(color=BLUE).scale(1.5)
        c = Circle(color=PURPLE).scale(1.5)
        self.play(Create(s))
        self.play(Transform(s, c))
        self.play(s.animate.rotate(PI / 4))
        self.wait(1)
