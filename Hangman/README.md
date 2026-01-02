# 🎮 Hangman Game

A classic word-guessing game with both console and GUI versions, featuring riddles as hints!

## 📝 Description

Hangman is a word puzzle game where players try to guess a word by suggesting letters within a limited number of guesses. This implementation includes both a traditional console-based version and a modern graphical user interface (GUI) version with helpful riddles.

## ✨ Features

### Console Version (`hangman.py`)
- Traditional command-line interface
- ASCII art hangman display
- 6 lives to guess the word
- Track guessed letters
- 216 challenging words

### GUI Version (`hangman_gui.py`)
- Modern, user-friendly graphical interface
- Dark themed design with colorful feedback
- 💡 **Riddle hints** for each word
- Visual hangman ASCII art display
- Lives counter and progress tracking
- Guessed letters display
- Input validation
- "New Game" button for quick restarts
- Win/lose message boxes
- Keyboard Enter key support for quick guessing

## 🚀 Installation

### Requirements
- Python 3.x
- tkinter (usually comes pre-installed with Python)

### Setup
1. Clone or download this repository
2. Ensure all files are in the same directory:
   - `hangman.py` (console version)
   - `hangman_gui.py` (GUI version)
   - `hangman_words.py` (word list)
   - `hangman_riddles.py` (riddles for each word)
   - `hangman_art.py` (ASCII art)

## 🎯 How to Play

### Running the Console Version
```bash
python hangman.py
```

### Running the GUI Version (Recommended)
```bash
python hangman_gui.py
```

### Game Rules
1. A random word is selected from the word list
2. You see a riddle/hint about the word
3. The word is displayed as underscores (e.g., `_ _ _ _ _`)
4. Guess one letter at a time
5. Correct guesses reveal the letter(s) in the word
6. Wrong guesses cost you a life (6 lives total)
7. Win by guessing all letters before running out of lives
8. Lose if you run out of lives

### Tips
- Read the riddle carefully - it's a clue about the word's meaning
- Start with common vowels (A, E, I, O, U)
- Look for common consonants (R, S, T, N, L)
- Pay attention to word length

## 📁 File Structure

```
Hangman/
│
├── hangman.py              # Console version of the game
├── hangman_gui.py          # GUI version with riddles (Recommended)
├── hangman_words.py        # List of 216 words to guess
├── hangman_riddles.py      # Riddles/hints for each word
├── hangman_art.py          # ASCII art for hangman stages and logo
├── README.md               # This file
└── __pycache__/            # Python cache files
```

## 🎨 GUI Features

### Color Scheme
- **Background**: Dark slate blue (#2C3E50)
- **Correct Guesses**: Green (#27AE60)
- **Wrong Guesses**: Red (#E74C3C)
- **Riddle Box**: Gray (#34495E)
- **Word Display**: Blue (#3498DB)

### Controls
- **Text Entry**: Type a single letter
- **Enter Key**: Submit your guess
- **Guess Button**: Click to submit your guess
- **New Game Button**: Start a fresh game

## 🏆 Word Categories

The game includes a diverse collection of words including:
- Everyday words with unusual spellings
- Musical instruments
- Natural phenomena
- Cultural references
- Scientific terms
- Animals and nature
- Food and drinks
- And much more!

## 🛠️ Technical Details

### Console Version
- Interactive command-line interface
- Simple input/output
- Clear screen formatting
- Lives tracking
- Letter tracking

### GUI Version
- Built with Python's tkinter library
- Event-driven programming
- Input validation
- Modal dialog boxes
- Responsive design
- Font customization

## 📚 Learning Outcomes

This project demonstrates:
- Python programming fundamentals
- GUI development with tkinter
- Game logic implementation
- Data structures (lists, dictionaries)
- User input validation
- Modular code design
- Random selection algorithms

## 🎓 Educational Value

Perfect for:
- Learning Python basics
- Understanding GUI programming
- Practicing vocabulary
- Logical thinking and problem-solving
- Code organization and modularity

## 🤝 Contributing

Feel free to enhance the game by:
- Adding more words and riddles
- Improving the GUI design
- Adding sound effects
- Implementing difficulty levels
- Adding multiplayer mode
- Creating themed word lists

## 📄 License

This project is open source and available for educational purposes.

## 🎉 Enjoy!

Have fun playing Hangman and expanding your vocabulary! Good luck with your guesses! 🍀

---

**Made with ❤️ using Python**
