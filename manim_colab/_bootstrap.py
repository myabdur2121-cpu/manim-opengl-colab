from __future__ import annotations

import os
import subprocess

from .system_deps import APT_SYSTEM, APT_MANIM

_bootstrapped = False
_xvfb_proc = None


def is_ready() -> bool:
    return _bootstrapped


def _apt_install(packages) -> None:
    subprocess.run(["apt-get", "update", "-qq"], check=False)
    subprocess.run(["apt-get", "install", "-y", "-qq", *packages], check=False)


def _start_xvfb() -> None:
    global _xvfb_proc
    if os.environ.get("DISPLAY"):
        return
    _xvfb_proc = subprocess.Popen(
        ["Xvfb", ":99", "-screen", "0", "1024x768x24"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    os.environ["DISPLAY"] = ":99"
    os.environ["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"


def ready(verbose: bool = True) -> None:
    global _bootstrapped
    if _bootstrapped:
        if verbose:
            print("--- ✅ manim_colab already ready ---")
        return

    if verbose:
        print("🛠️  First-time setup: installing system packages + virtual display ...")
    _apt_install(APT_SYSTEM)
    _start_xvfb()
    _apt_install(APT_MANIM)
    from . import magic
    magic.apply_opengl_patches()

    _bootstrapped = True
    if verbose:
        print("--- 🚀 manim_colab ready: GPU OpenGL engine is live. ---")


def _manim_lazy(line, cell):
    ready()
    from .magic import run_scene_inline
    return run_scene_inline(line, cell)


def register_magic() -> None:
    try:
        from IPython import get_ipython
    except ImportError:
        return
    ip = get_ipython()
    if ip is None:
        return
    ip.register_magic_function(_manim_lazy, magic_kind="cell", magic_name="manim")
