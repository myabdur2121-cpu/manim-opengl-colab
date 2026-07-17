from __future__ import annotations
import os
import subprocess

_xvfb_proc = None


def start_xvfb(verbose: bool = True) -> None:
    """Start Xvfb and set DISPLAY — IN THE KERNEL (must not be a subprocess)."""
    global _xvfb_proc

    if os.environ.get("DISPLAY"):
        if verbose:
            print(f"✅ [Cell 2] DISPLAY already set → {os.environ['DISPLAY']}")
        return

    if verbose:
        print("🖥️  [Cell 2] Starting Xvfb virtual display (:99) ...")

    _xvfb_proc = subprocess.Popen(
        ["Xvfb", ":99", "-screen", "0", "1024x768x24"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    os.environ["DISPLAY"] = ":99"
    os.environ["__GLX_VENDOR_LIBRARY_NAME"] = "nvidia"

    if verbose:
        print("✅ [Cell 2] Virtual display ready (DISPLAY=:99).")
