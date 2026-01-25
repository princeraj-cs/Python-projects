# Turtle Crossing

A simple Frogger-style arcade mini-game built with Python's `turtle` module. Guide the turtle from the bottom of the screen to the top while dodging a stream of cars. Each successful crossing increases the level and makes traffic denser.

## How to Run
1. Install Python 3.8+ (the standard library `turtle` module is included).
2. From the project root, run:
   ```bash
   cd Turtle_crossing
   python main.py
   ```

## Controls
- **Up Arrow**: Move the turtle forward (upwards).
- Click the window to close after game over.

## Gameplay Notes
- Cars spawn at random lanes with random colors.
- Collision is detected when a car comes within a small distance of the player.
- Reaching the top resets the player to the start and increments the level; traffic generation becomes more aggressive.

## Project Structure
- `main.py` — sets up the screen, game loop, input handling, and collision checks.
- `player.py` — defines the turtle player (movement and finish-line detection).
- `car_manager.py` — handles car creation, speed, and movement.
- `scoreboard.py` — draws the current level and game-over text.

## Tweaks
- Adjust spawn rate: change the `random_chance` logic in `car_manager.py`.
- Adjust speed: modify `STARTING_MOVE_DISTANCE` or `MOVE_INCREMENT` in `car_manager.py`, and `MOVE_DISTANCE` in `player.py`.
- Change finish line: update `FINISH_LINE_Y` in `player.py`.

## Troubleshooting
- If the window closes immediately, run the script from a terminal so errors stay visible.
- On some Linux setups, `python-tk`/`tkinter` may need to be installed separately.

Enjoy the crossing! 🎮
