# ManimCE OpenGL on Google Colab · GPU

> 📖 **New to this? Read the [Quick Start](QUICKSTART.md) — 3 cells, done.**

> Render ManimCE animations with the **OpenGL renderer**, headlessly, inside
> **Google Colab** — video embedded inline + a one-click download button.
> **Open the notebook, set runtime to T4 GPU, Run all.**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/myabdur2121-cpu/manim-opengl-colab/blob/main/notebooks/00_Manim_OpenGL_Colab.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## What this is

Google Colab has **no display**, so ManimCE's OpenGL renderer does not work out
of the box. This repo packages a tested setup that spins up a **virtual display**
(Xvfb), installs **ManimCE + LaTeX**, applies **OpenGL patches**, and registers
a `%%manim` magic that renders inline.

## Quick start (3 ways)

### A) One line (recommended)

```python
!pip install -q manim moderngl numpy matplotlib
!pip install -q --no-deps git+https://github.com/myabdur2121-cpu/manim-opengl-colab
import manim_colab

%%manim -ql --renderer=opengl --write_to_movie True MyScene
from manim import *
class MyScene(Scene):
    def construct(self):
        self.play(Create(Square()))
        self.wait(1)
```

The first `%%manim` call auto-runs the one-time setup (apt + Xvfb + LaTeX).
Later calls are fast.

### B) Clone + Run all

Click the Open in Colab badge above, set **Runtime → T4 GPU → Run all**.

### C) Use the package

```python
from manim_colab import install_all, setup_and_verify, register_manim_magic
install_all()
setup_and_verify()
register_manim_magic()
```

## Prerequisite

**Runtime → Change runtime type → Hardware accelerator → T4 GPU → Save**

## The 9 stages

| Stage | Purpose |
|:-----:|----------|
| 0 | nvidia-smi pre-flight GPU check |
| 1 | apt: xvfb + GL libs / pip: moderngl numpy matplotlib |
| 2 | start Xvfb, set DISPLAY |
| 3 | moderngl context + GL verification |
| 4 | offscreen FBO render test (matplotlib) |
| 5 | apt: LaTeX + Cairo / pip: manim IPython==8.21.0 |
| 6 | config.media_embed = True |
| 7 | OpenGL patches + SceneFileWriter fixes + %%manim magic |
| 8 | render scene inline |
| 9 | download the .mp4 |

## Reusing your own effects

Because `%%manim` compiles each cell in isolation, define your effects in a
`.py` file and import them:

```python
open("my_effects.py", "w").write("""
from manim import *
class PopIn(GrowFromCenter): pass
""")

%%manim -ql --renderer=opengl --write_to_movie True Demo
from my_effects import PopIn
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `XOpenDisplay: cannot open display` | Run setup (stages 1-2) first |
| Render finishes but no video | Add `--write_to_movie True` |
| Render hangs | Ensure GPU runtime + stage 2 ran |
| TeX errors | Re-run stage 5 (texlive) |

## Architectural note

Xvfb provides **software** OpenGL (Mesa/llvmpipe), so animations render reliably
on the CPU. To truly use the T4 GPU, use EGL backend
(`moderngl.create_context(backend='egl')`) + the built-in `%%manim` magic.
The Xvfb path is the reliable default.

## License

MIT — see LICENSE.
