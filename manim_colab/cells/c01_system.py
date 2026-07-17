from __future__ import annotations
import subprocess

# Essential system libraries. ORDER MATTERS:
#   - xvfb, libgl1-mesa-glx, libglapi-mesa  -> virtual display + GL
#   - libcairo2-dev, libpango1.0-dev        -> MUST be before pip install manim
#                                               (pycairo/ManimPango build from source)
#   - ffmpeg                                -> video stitching
APT_ESSENTIAL = [
    "xvfb",
    "libgl1-mesa-glx",
    "libglapi-mesa",
    "libcairo2-dev",
    "libpango1.0-dev",
    "ffmpeg",
]

# LaTeX (TeX Live) — needed ONLY for MathTex / Tex. Big + slow (~3 min).
APT_LATEX = [
    "texlive",
    "texlive-latex-extra",
    "texlive-fonts-extra",
    "texlive-latex-recommended",
    "texlive-science",
    "tipa",
]


def apt_install(verbose: bool = True, with_latex: bool = True) -> None:
    if verbose:
        print("📦 [Cell 1] apt-get update + installing system libraries ...")

    packages = list(APT_ESSENTIAL)
    if with_latex:
        packages += APT_LATEX

    subprocess.run(["apt-get", "update", "-qq"], check=False)
    subprocess.run(["apt-get", "install", "-y", "-qq", *packages], check=False)

    if verbose:
        print("✅ [Cell 1] System libraries installed." + (" (LaTeX included)" if with_latex else " (no LaTeX)"))
