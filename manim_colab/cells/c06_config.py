from __future__ import annotations


def enable_embed(verbose: bool = True) -> None:
    """Set config.media_embed = True so rendered videos show inline."""
    if verbose:
        print("⚙️  [Cell 6] Enabling inline video embed (media_embed = True) ...")
    import manim
    manim.config.media_embed = True
    if verbose:
        print("✅ [Cell 6] media_embed enabled.")
