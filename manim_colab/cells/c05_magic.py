from __future__ import annotations


def register_magic(verbose: bool = True) -> None:
    """Apply OpenGL patches and register our %%manim magic — IN THE KERNEL.

    THE CONFLICT FIX:
        Importing `manim` auto-registers manim's OWN built-in %%manim magic,
        which OVERRIDES ours. So we import manim FIRST, then register OUR
        magic AFTER, so ours wins. Without this, %%manim runs manim's magic
        and throws KeyError: ''.
    """
    if verbose:
        print("🪄 [Cell 5] OpenGL patches + %%manim magic registration ...")

    # 1. Import manim — this triggers manim's built-in %%manim registration.
    import manim

    # 2. Apply our OpenGL engine patches (write_frame, combine_to_movie, mobject attrs).
    from ..engine import apply_opengl_patches, run_scene_inline
    apply_opengl_patches()

    # 3. Re-register OUR magic ON TOP of manim's. This is the fix!
    def _our_manim(line, cell):
        return run_scene_inline(line, cell)

    try:
        from IPython import get_ipython
        ip = get_ipython()
        if ip is not None:
            ip.register_magic_function(_our_manim, magic_kind="cell", magic_name="manim")
            if verbose:
                print("✅ [Cell 5] %%manim magic registered (OpenGL path, overrides manim's).")
        else:
            if verbose:
                print("⚠️  [Cell 5] No IPython kernel — skipped (this is normal outside Colab).")
    except ImportError:
        if verbose:
            print("⚠️  [Cell 5] IPython not available — skipped.")
