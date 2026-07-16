# Examples

Standalone ManimCE scenes. Render via the `%%manim` magic or the CLI helper.

| Scene | Shows |
|-------|-------|
| `SquareToCircle` | Create, Transform, .animate rotate + shift |
| `GPUAnimationTest` | the master-notebook stage-8 scene |
| `Formula` | MathTex LaTeX (needs TeX Live) |

```bash
# In a notebook:
%%manim -ql --renderer=opengl --write_to_movie True SquareToCircle

# CLI:
./scripts/run_locally.sh examples/01_square_to_circle.py SquareToCircle
```
