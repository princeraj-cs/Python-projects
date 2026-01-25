# Pong (Turtle Graphics)

> Note: Despite the folder name "Turtle_crossing", the current code implements a classic Pong game built with Python's `turtle` module. This README documents the project as it exists.

## Overview
A simple two-player Pong clone using Python's standard `turtle` graphics. The ball bounces off the top/bottom walls and paddles. A player scores when the opponent misses the ball. The ball speeds up slightly on each paddle hit.

## Controls
- Right paddle: `Up` and `Down`
- Left paddle: `W` and `S`

## How to Run
Requirements: Python 3.x (no external packages needed).

On Windows/macOS/Linux, from the repository root:

```bash
python Turtle_crossing/main.py
```

A window titled "Pong" will open. Close it or click once in the window to exit.

## Files
- [main.py](./main.py): Game loop, input binding, collision/score handling.
- [paddle.py](./paddle.py): `Paddle` class for player paddles.
- [ball.py](./ball.py): `Ball` class for movement, bounces, and speed.
- [score.py](./score.py): `Scoreboard` class for rendering scores.

## Gameplay Notes
- The ball reverses Y direction on wall hits.
- The ball reverses X direction on paddle hits and accelerates slightly.
- Right player scores when the ball passes the left paddle; left player scores when it passes the right paddle.

## Troubleshooting
- If the window doesn’t update smoothly, ensure the terminal stays focused and do not resize the window rapidly.
- `turtle` is part of the Python standard library; if it’s missing, verify you’re using a full CPython install (not a minimal runtime).

## Next Steps (Optional)
- Add winning score and game over screen.
- Add paddle movement limits to keep paddles on screen.
- Add sound effects and a start/pause screen.