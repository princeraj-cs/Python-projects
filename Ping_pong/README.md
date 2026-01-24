# 🏓 Ping Pong (Turtle)

Classic two-player Pong built with Python's built-in `turtle` module.

## 🎮 How to Play
- Player 1 (left paddle): `W` to move up, `S` to move down.
- Player 2 (right paddle): `Up Arrow` to move up, `Down Arrow` to move down.
- Keep the ball in play; missing the ball awards a point to the opponent.

## ▶️ Running Locally
1. Ensure Python 3.x is installed (the `turtle` module ships with the standard library on most desktop distributions).
2. From the project root, run:

   ```bash
   python Ping_pong/main.py
   ```

## 🗂️ Project Structure
- `main.py` — sets up the screen, paddles, ball loop, and collision/score handling.
- `paddle.py` — paddle behavior and movement.
- `ball.py` — ball motion and wall/paddle bounce logic.
- `score.py` — scoreboard rendering and point tracking.

## ⚡ Gameplay Notes
- The ball accelerates slightly after each paddle hit, upping the challenge.
- The window closes when you click inside the game window after you finish playing.

## 🛠️ Troubleshooting
- If the window does not appear, ensure you are running the script from a desktop environment (the `turtle` module requires GUI support).
