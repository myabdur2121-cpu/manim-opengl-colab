from ._bootstrap import ready, is_ready, register_magic

register_magic()

from .system_deps import install_system_deps, install_manim, install_all
from .gpu import (
    setup_xvfb,
    make_gl_context,
    print_gpu_info,
    render_solid_frame,
    setup_and_verify,
)
from .magic import (
    enable_inline_embed,
    apply_opengl_patches,
    run_scene_inline,
    register_manim_magic,
)

__version__ = "1.1.0"

__all__ = [
    "ready",
    "is_ready",
    "register_magic",
    "install_system_deps",
    "install_manim",
    "install_all",
    "setup_xvfb",
    "make_gl_context",
    "print_gpu_info",
    "render_solid_frame",
    "setup_and_verify",
    "enable_inline_embed",
    "apply_opengl_patches",
    "run_scene_inline",
    "register_manim_magic",
]
