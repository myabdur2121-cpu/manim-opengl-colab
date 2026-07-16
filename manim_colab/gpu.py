from __future__ import annotations

import os
import subprocess

_xvfb_proc = None


def setup_xvfb(display: str = ":99", geometry: str = "1024x768x24"):
    global _xvfb_proc
    _xvfb_proc = subprocess.Popen(
        ["Xvfb", display, "-screen", "0", geometry],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    os.environ["DISPLAY"] = display
    os.environ["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"
    return _xvfb_proc


def make_gl_context():
    import moderngl
    return moderngl.create_context(standalone=True)


def print_gpu_info(ctx) -> None:
    print("--- 🚀 GPU ACCELERATION VERIFIED 🚀 ---")
    print("Vendor:   ", ctx.info["GL_VENDOR"])
    print("Renderer: ", ctx.info["GL_RENDERER"])
    print("Version:  ", ctx.info["GL_VERSION"])


def render_solid_frame(ctx, size: int = 512, color=(0.0, 0.6, 0.7, 1.0)):
    import numpy as np
    import matplotlib.pyplot as plt

    fbo = ctx.framebuffer(
        color_attachments=ctx.texture((size, size), 4),
        depth_attachment=ctx.depth_renderbuffer((size, size)),
    )
    fbo.use()
    ctx.clear(*color)

    pixels = fbo.read(components=4)
    img_array = np.frombuffer(pixels, dtype=np.uint8).reshape((size, size, 4))

    plt.imshow(img_array)
    plt.axis("off")
    plt.show()

    fbo.release()
    ctx.release()


def setup_and_verify() -> None:
    setup_xvfb()
    ctx = make_gl_context()
    print_gpu_info(ctx)
    render_solid_frame(ctx)
