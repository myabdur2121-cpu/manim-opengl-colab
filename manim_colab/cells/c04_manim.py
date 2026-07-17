from __future__ import annotations
import subprocess
import sys

# Installed AFTER c01 (cairo/pango must be present first for the build).
PIP_PACKAGES = ["manim", "moderngl", "numpy", "matplotlib"]


def install_manim(verbose: bool = True) -> None:
    if verbose:
        print("🐍 [Cell 4] Installing Python packages (manim + moderngl + numpy + matplotlib) ...")

    # Skip if manim is already importable (e.g. pip install git+ already pulled it).
    try:
        import manim  # noqa
        if verbose:
            print(f"✅ [Cell 4] manim already installed (v{manim.__version__}).")
        return
    except ImportError:
        pass

    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-q", *PIP_PACKAGES],
        check=False,
    )
    if verbose:
        print("✅ [Cell 4] Python packages installed.")
