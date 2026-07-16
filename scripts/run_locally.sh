#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <scene_file.py> <SceneClassName> [extra manim flags]"
  exit 1
fi

FILE="$1"
SCENE="$2"
shift 2

xvfb-run -a manim --renderer=opengl --write_to_movie "$@" "$FILE" "$SCENE"
