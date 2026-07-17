from __future__ import annotations

import os
import subprocess


def enable_inline_embed() -> None:
    import manim
    manim.config.media_embed = True


def _patch_opengl_mobjects() -> None:
    import manim.mobject.mobject
    import manim.mobject.opengl.opengl_mobject
    manim.mobject.mobject.Mobject.z_index = 0
    manim.mobject.opengl.opengl_mobject.OpenGLMobject.z_index = 0
    manim.mobject.mobject.Mobject.should_render = True
    manim.mobject.opengl.opengl_mobject.OpenGLMobject.should_render = True


def _patch_scene_file_writer() -> None:
    import numpy as np
    import manim
    from manim.scene.scene_file_writer import SceneFileWriter

    def patched_write_frame(self, frame_or_renderer, num_frames=1):
        if not manim.config.write_to_movie:
            return
        if isinstance(frame_or_renderer, np.ndarray):
            frame = frame_or_renderer
        else:
            frame = frame_or_renderer.get_frame()
        if not isinstance(frame, np.ndarray):
            frame = np.array(frame, dtype=np.uint8)
        self.queue.put((num_frames, frame))

    SceneFileWriter.write_frame = patched_write_frame

    def custom_combine_to_movie(self):
        partial_files = self.partial_movie_files
        if not partial_files:
            return
        os.makedirs(os.path.dirname(self.movie_file_path), exist_ok=True)
        txt_path = os.path.join(os.path.dirname(self.movie_file_path), "manifest.txt")
        with open(txt_path, "w") as f:
            for pf in partial_files:
                f.write(f"file '{os.path.abspath(pf)}'\n")
        output_file = os.path.abspath(self.movie_file_path)
        cmd = f"ffmpeg -y -f concat -safe 0 -i {txt_path} -c copy '{output_file}'"
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    SceneFileWriter.combine_to_movie = custom_combine_to_movie


def apply_opengl_patches() -> None:
    _patch_opengl_mobjects()
    _patch_scene_file_writer()
    enable_inline_embed()


def run_scene_inline(line, cell):
    """Compile + render a scene with OpenGLRenderer; return an inline Video."""
    import manim
    from IPython.display import Video

    parts = line.split()
    scene_name = parts[-1]

    manim.config.pixel_width = 1280
    manim.config.pixel_height = 720
    manim.config.frame_rate = 30
    manim.config.video_dir = "./media/videos/inline_scene/720p30"
    manim.config.media_dir = "./media"
    manim.config.write_to_movie = True
    manim.config.renderer = 'opengl'   # LOCK renderer across the pipeline

    os.makedirs(
        f"./media/videos/inline_scene/720p30/partial_movie_files/{scene_name}",
        exist_ok=True,
    )

    exec(cell, globals())

    from manim.renderer.opengl_renderer import OpenGLRenderer
    SceneClass = globals()[scene_name]
    scene_instance = SceneClass(renderer=OpenGLRenderer())
    scene_instance.render()

    target_video = f"./media/videos/inline_scene/720p30/{scene_name}.mp4"
    if os.path.exists(target_video):
        print(f"--- 🚀 GPU ACCELERATED RENDER SUCCESSFUL ({scene_name}) 🚀 ---")
        return Video(target_video, embed=True, width=640, height=360)

    alt_path = f"./media/videos/scene/720p30/{scene_name}.mp4"
    if os.path.exists(alt_path):
        print(f"--- 🚀 GPU ACCELERATED RENDER SUCCESSFUL ({scene_name}) 🚀 ---")
        return Video(alt_path, embed=True, width=640, height=360)

    print("Video rendering finished but file output path validation failed.")
