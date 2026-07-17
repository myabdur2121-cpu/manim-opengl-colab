# ManimCE OpenGL on Google Colab · GPU

> Render ManimCE animations with the **OpenGL renderer**, headlessly, inside
> **Google Colab** — video embedded inline + a one-click download button.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Quick start

1. **Runtime → Change runtime type → Hardware accelerator → T4 GPU → Save**
2. **Cell 1:**
   ```python
   !pip install -q git+https://github.com/myabdur2121-cpu/manim-opengl-colab
   import manim_colab; manim_colab.ready()
   ```
3. **Cell 2:**
   ```python
   %%manim MyScene
   from manim import *
   class MyScene(Scene):
       def construct(self):
           self.play(Create(Square()))
           self.wait(1)
   ```
4. **Cell 3:**
   ```python
   from google.colab import files
   files.download("./media/videos/inline_scene/720p30/MyScene.mp4")
   ```

The first `%%manim` call (or `ready()`) runs all setup cells **in the kernel**:
system libs → Xvfb → GPU verify → manim install → OpenGL patches + magic → embed.

## How it works (architecture)

The setup runs as Python imports inside the live IPython kernel — **not** as a
bash subprocess. This is critical: Xvfb must stay alive, DISPLAY must be set in
the kernel, and the `%%manim` magic must be registered in the kernel. A bash
script `setup_all.sh` would die and lose all of this.

```
ready()  runs in-kernel, in order:
  c01 apt_install()      ← subprocess (persists to disk — OK)
  c02 start_xvfb()       ← kernel (Xvfb stays alive + DISPLAY set)
  c03 verify_gpu()       ← kernel (moderngl context)
  c04 install_manim()    ← subprocess (persists to disk — OK)
  c05 register_magic()   ← kernel (patches + %%manim, after manim's own)
  c06 enable_embed()     ← kernel (media_embed = True)
```

## License

MIT.
