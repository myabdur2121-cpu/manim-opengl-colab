from __future__ import annotations

_bootstrapped = False


def is_ready() -> bool:
    return _bootstrapped


def ready(verbose: bool = True, with_latex: bool = True) -> None:
    """Run ALL setup cells in-kernel, in the correct order.

    This is the ONLY function a user needs to call. It runs each cell as a
    Python import inside the live IPython kernel (NOT a bash subprocess), so
    Xvfb stays alive, DISPLAY is set, the %%manim magic is registered, and
    config.media_embed is set — all in the kernel that will render scenes.
    """
    global _bootstrapped
    if _bootstrapped:
        if verbose:
            print("✅ manim_colab already ready (setup ran earlier).")
        return

    from .cells import (
        c01_system, c02_display, c03_gpu,
        c04_manim, c05_magic, c06_config,
    )

    print("=" * 60)
    print("🚀 manim_colab.ready() — running all cells IN-KERNEL")
    print("=" * 60)

    c01_system.apt_install(verbose, with_latex=with_latex)
    c02_display.start_xvfb(verbose)
    c03_gpu.verify_gpu(verbose)
    c04_manim.install_manim(verbose)
    c05_magic.register_magic(verbose)
    c06_config.enable_embed(verbose)

    _bootstrapped = True
    print("=" * 60)
    print("🎉 ALL SETUP COMPLETE — now write %%manim in any cell.")
    print("=" * 60)


def _manim_lazy(line, cell):
    """Lazy %%manim: if ready() wasn't called, run it first, then render."""
    ready()
    from .engine import run_scene_inline
    return run_scene_inline(line, cell)


def register_magic() -> None:
    """Register a lazy %%manim magic on import (no-op outside a kernel)."""
    try:
        from IPython import get_ipython
    except ImportError:
        return
    ip = get_ipython()
    if ip is None:
        return
    ip.register_magic_function(_manim_lazy, magic_kind="cell", magic_name="manim")


# Auto-register on import — harmless no-op outside a kernel.
register_magic()
