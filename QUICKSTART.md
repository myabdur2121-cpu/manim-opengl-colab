# Quick Start

## ১. Runtime সেট করুন
Runtime → Change runtime type → T4 GPU → Save

## ২. সেল ১ — ইনস্টল + সেটআপ (একসাথে)
```python
!pip install -q git+https://github.com/myabdur2121-cpu/manim-opengl-colab
import manim_colab; manim_colab.ready()
```

## ৩. সেল ২ — অ্যানিমেশন
```python
%%manim MyScene
from manim import *

class MyScene(Scene):
    def construct(self):
        s = Square(color=BLUE).scale(1.5)
        c = Circle(color=PURPLE).scale(1.5)
        self.play(Create(s))
        self.play(Transform(s, c))
        self.wait(1)
```

## ৪. সেল ৩ — ডাউনলোড
```python
from google.colab import files
files.download("./media/videos/inline_scene/720p30/MyScene.mp4")
```

`myabdur2121-cpu` আপনার GitHub নাম দিন।
