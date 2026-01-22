# Snake Game

A classic Snake Game built with Python using the Turtle graphics library. Navigate the snake to eat food, grow longer, and achieve the highest score possible!

## Overview

This is a recreated version of the timeless Snake game where players control a snake that moves around a bounded arena, eats food, and grows in length. The game ends if the snake collides with the walls or itself.

## Game Features

- **Snake Movement**: Control the snake using arrow keys (Up, Down, Left, Right)
- **Food Collection**: Navigate to red food squares to grow your snake and increase your score
- **Score Tracking**: Real-time score display at the top of the game screen
- **Collision Detection**: 
  - Wall collision ends the game
  - Self-collision (hitting your own tail) ends the game
- **Smooth Gameplay**: Consistent frame rate for responsive controls

## Requirements

- Python 3.x
- Turtle graphics library (included with Python)

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. No additional packages need to be installed (Turtle is part of the standard library)

## How to Run

Execute the main script from your terminal or command prompt:

```bash
python main.py
```

The game window will open with a 600x600 pixel black arena. Use the arrow keys to control the snake.

## Game Controls

| Key | Action |
|-----|--------|
| **↑ Up Arrow** | Move snake up |
| **↓ Down Arrow** | Move snake down |
| **← Left Arrow** | Move snake left |
| **→ Right Arrow** | Move snake right |

## File Structure

- **main.py** - Main game loop and event handling
  - Sets up the game screen
  - Initializes snake, food, and scoreboard
  - Handles collision detection
  - Manages game state

- **snake.py** - Snake class
  - Manages snake segments
  - Handles movement logic
  - Implements snake growth (extend function)

- **food.py** - Food class
  - Generates random food positions
  - Refreshes food location when eaten

- **scoreboard.py** - Scoreboard class
  - Tracks player score
  - Displays score on screen
  - Shows game over message

## Game Mechanics

### Movement
- The snake moves continuously in the current direction
- Each direction change is applied on the next game tick

### Food
- Red circular food appears at random positions on the screen
- Eating food extends the snake by one segment
- Food respawns at a new random location after being eaten

### Scoring
- Gain 1 point for each food item eaten
- Score is displayed in the top-center of the screen

### Game Over
- Hitting the boundary walls ends the game
- Colliding with your own tail ends the game
- "Game Over" message is displayed when the game ends

## Future Enhancements

Potential improvements for future versions:
- Increasing difficulty/speed as score increases
- High score tracking and persistence
- Different difficulty levels
- Sound effects and visual effects
- Mobile/touch support

## License

This project is open source and available for educational purposes.

## Author

Created as a classic Python game project using Turtle graphics.
