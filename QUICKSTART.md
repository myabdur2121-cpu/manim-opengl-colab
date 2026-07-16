# Quick Start

## 1. Runtime সেট করুন
Runtime → Change runtime type → T4 GPU → Save

## 2. সেল 1 — ইনস্টল
```python
!pip install -q git+https://github.com/myabdur2121-cpu/manim-opengl-colab
import manim_colab
```

## 3. সেল 2 — অ্যানিমেশন
```python
%%manim -ql --renderer=opengl --write_to_movie True MyScene
from manim import *

class MyScene(Scene):
    def construct(self):
        s = Square(color=BLUE).scale(1.5)
        c = Circle(color=PURPLE).scale(1.5)
        self.play(Create(s))
        self.play(Transform(s, c))
        self.wait(1)
```

প্রথমবার ৫-১০ মিনিট লাগবে (auto setup)। এরপর ভিডিও ইনলাইন দেখাবে।

## 4. সেল 3 — ডাউনলোড
```python
from google.colab import files
files.download("./media/videos/inline_scene/720p30/MyScene.mp4")
```

ব্যস! আপনার GitHub নাম ব্যবহার করে সব কিছু সেটআপ হয়ে যাবে।
