from __future__ import annotations


def verify_gpu(verbose: bool = True) -> None:
    """Create a moderngl context and print GL info. Non-fatal if it fails."""
    if verbose:
        print("🔍 [Cell 3] Verifying OpenGL context ...")
    try:
        import moderngl
        ctx = moderngl.create_context(standalone=True)
        info = ctx.info
        if verbose:
            print(f"      Vendor:   {info.get('GL_VENDOR', '?')}")
            print(f"      Renderer: {info.get('GL_RENDERER', '?')}")
            print(f"      Version:  {info.get('GL_VERSION', '?')}")
        ctx.release()
        print("✅ [Cell 3] OpenGL context verified.")
    except Exception as e:
        if verbose:
            print(f"⚠️  [Cell 3] GPU verify skipped (non-fatal): {e}")
