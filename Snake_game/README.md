# 🐍 Snake Game

> A classic Snake Game implementation in Python using the Turtle graphics library. Navigate your snake to eat food, grow longer, and compete for the highest score!

## 🎮 Overview

This is a fully-featured recreation of the timeless Snake arcade game. Control a growing snake through a bounded arena, collect food to increase your score, and avoid collisions with walls and your own tail. Built with pure Python and the standard Turtle graphics library—no external dependencies required!

## ✨ Features

- **🎯 Snake Movement**: Smooth, responsive arrow key controls (Up, Down, Left, Right)
- **🍎 Food Mechanics**: Randomly spawning food that grows your snake by one segment per consumption
- **📊 Real-time Score Tracking**: Score display at the top-center of the game window
- **💥 Collision Detection**: 
  - Wall collisions end the game
  - Self-collision (hitting your own tail) ends the game
  - Instant game-over message display
- **⚡ Optimized Performance**: Consistent 10 FPS for smooth, responsive gameplay
- **🎨 Clean UI**: Black game arena with white snake and red food for clear visibility

## 📋 Requirements

- **Python**: 3.6 or higher
- **Turtle Graphics**: Built-in with Python (no installation needed)
- **OS**: Windows, macOS, or Linux

## 🚀 Quick Start

### Installation
```bash
# Clone or download this repository
git clone <repository-url>
cd Snake_game
```

### Running the Game
```bash
python main.py
```

The game window will launch with a 600×600 pixel black arena. Use your arrow keys to control the snake!

## 🎮 How to Play

| Key | Action |
|:---:|:------:|
| **↑** | Move snake up |
| **↓** | Move snake down |
| **←** | Move snake left |
| **→** | Move snake right |

### Objective
- **Eat Food**: Move your snake's head over the red food squares
- **Grow**: Your snake grows by one segment with each food eaten
- **Score**: Earn 1 point per food consumed
- **Survive**: Avoid walls and your own tail to keep playing

## 📁 Project Structure

```
Snake_game/
├── main.py           # Game loop, screen setup, and collision detection
├── snake.py          # Snake class with movement and growth logic
├── food.py           # Food class with random position generation
├── scoreboard.py     # Score tracking and display
└── README.md         # This file
```

### File Details

**`main.py`** (Main Game Logic)
- Initializes the 600×600 game screen
- Creates and manages game objects (snake, food, scoreboard)
- Implements the main game loop (10 FPS)
- Handles all collision detection logic
- Updates display and manages game state

**`snake.py`** (Snake Class)
- Manages snake segments as a list of Turtle objects
- Handles directional movement (up, down, left, right)
- Implements snake growth when food is eaten
- Tracks the snake's head position for collision detection

**`food.py`** (Food Class)
- Generates random food positions within the game arena
- Respawns food at new locations when eaten
- Inherits from Turtle for easy rendering

**`scoreboard.py`** (Scoreboard Class)
- Tracks cumulative score throughout the game
- Displays score in real-time on screen
- Shows "GAME OVER" message when the game ends

## 🎮 Game Mechanics

### Movement System
- Snake moves continuously in its current direction
- New directional inputs queue and apply on the next game tick
- Movement prevents reversing into yourself (prevents instant self-collision)

### Food System
- Red circular food spawns at random coordinates
- Food is placed at random positions within the play area
- Eating food adds one new segment to the snake's tail
- New food appears immediately after consumption

### Scoring System
- Score increments by 1 for each food item eaten
- Score persists throughout the game session
- Final score displays in the "GAME OVER" message

### Collision Detection
- **Wall Collision**: Snake hits the arena boundary (±280 pixels from center)
- **Self-Collision**: Snake's head touches any segment of its own body
- Either collision type triggers immediate game over

## 💡 Game Tips

- **Plan Ahead**: Don't box yourself into a corner—always think two moves ahead
- **Edge Control**: Use the walls strategically to create space
- **Pattern Recognition**: Develop consistent patterns for collecting food efficiently
- **Stay Calm**: The snake moves at a fixed speed, so you have time to react

## 🔄 Game Flow

```
1. Start → Initialize snake (3 segments), food, score
2. Update → Move snake in current direction
3. Collect → Check food collision, grow snake, update score
4. Detect → Check wall and self-collision
5. Render → Update screen display
6. Repeat steps 2-5 until collision occurs
7. Game Over → Display final score, wait for window close
```

## 🚀 Future Enhancements

Potential improvements for future versions:
- **Progressive Difficulty**: Increase speed as score increases
- **High Score Persistence**: Save and load best scores from file
- **Multiple Difficulty Levels**: Easy, Normal, Hard modes
- **Visual Enhancements**: Color effects, animations, themes
- **Sound Effects**: Background music and sound effects
- **Mobile Support**: Touch screen controls for mobile devices
- **Pause Functionality**: Pause and resume mid-game
- **Special Power-ups**: Temporary speed boost or invincibility items

## 📝 Code Style

This project follows Python best practices:
- Clear, descriptive class and method names
- Modular design with separation of concerns
- Object-oriented architecture for extensibility
- Comments for complex logic sections

## 📄 License

This project is open source and available for educational and personal use.

## 👤 Author

Created as a Python learning project demonstrating:
- Object-oriented programming (OOP)
- Game loop implementation
- Event handling and controls
- Collision detection algorithms
- Use of Python's standard Turtle graphics library

---

**Enjoy the game and happy coding! 🎮**
