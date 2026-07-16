from __future__ import annotations

import subprocess
import sys
from typing import List

APT_SYSTEM: List[str] = ["xvfb", "libgl1-mesa-glx", "libglapi-mesa"]
PIP_GL: List[str] = ["moderngl", "numpy", "matplotlib"]

APT_MANIM: List[str] = [
    "libcairo2-dev",
    "texlive",
    "texlive-latex-extra",
    "texlive-fonts-extra",
    "texlive-latex-recommended",
    "texlive-science",
    "tipa",
    "libpango1.0-dev",
]


def _run(cmd: List[str]) -> None:
    print("$", " ".join(cmd))
    subprocess.run(cmd, check=False)


def install_system_deps() -> None:
    _run(["apt-get", "update", "-qq"])
    _run(["apt-get", "install", "-qq", *APT_SYSTEM])
    _run([sys.executable, "-m", "pip", "install", "-q", *PIP_GL])


def install_manim() -> None:
    _run(["sudo", "apt", "update"])
    _run(["sudo", "apt", "install", *APT_MANIM])
    _run([sys.executable, "-m", "pip", "install", "manim"])
    _run([sys.executable, "-m", "pip", "install", "IPython==8.21.0"])


def install_all() -> None:
    install_system_deps()
    install_manim()
