# 🗺️ US States Guess Game

An interactive educational game that challenges you to name all 50 US states on a blank map. Test your geography knowledge and learn the locations of states you might have forgotten!

## 🎮 Features

- **Interactive Map**: Click on states or type their names to mark them on the map
- **Progress Tracking**: See how many states you've correctly identified out of 50
- **Real-time Feedback**: Instantly know if your answer is correct and where the state is located
- **Learning Mode**: Generate a "remember.csv" file with states you missed for later study
- **User-Friendly**: Type state names naturally—the game handles formatting automatically
- **Easy Exit**: Type "Exit" at any time to quit the game

## 📋 Requirements

- Python 3.x
- `turtle` (usually included with Python)
- `pandas`

## 🚀 Installation

1. Clone or download this project
2. Install required dependencies:
   ```bash
   pip install pandas
   ```
3. Ensure `50_states.csv` and `blank_states_img.gif` are in the same directory as `main.py`

## 📂 Files

- **main.py**: Main game logic
- **50_states.csv**: CSV file containing all 50 US states with their coordinates (x, y) on the map
- **blank_states_img.gif**: The blank US map image used as the game backdrop
- **remember.csv**: Auto-generated file containing states you missed (for study purposes)

## 🎯 How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. A window will open showing a blank US map

3. A dialog box will prompt you to enter a state name

4. Type the name of any US state (e.g., "California", "Texas", "Florida")

5. If correct:
   - The state name appears on the map at its correct location
   - Your progress counter increases
   - You're prompted to enter another state

6. Repeat until you've named all 50 states or type "Exit" to quit

7. After exiting, a `remember.csv` file is created listing states you didn't guess

## 💡 Tips

- You don't need to worry about capitalization—just type naturally!
- If you can't remember a state, skip it and try others
- Use the generated `remember.csv` to study states you missed
- Take your time and enjoy learning US geography!

## 🎓 Educational Value

Perfect for students learning:
- US state capitals and locations
- Geography and spatial awareness
- State boundaries and regional groupings
- Interactive Python programming concepts

## 📊 CSV Format

**50_states.csv** contains:
- `state`: Name of the state
- `x`: X-coordinate on the map
- `y`: Y-coordinate on the map

## 🔧 Troubleshooting

- **Map image not showing**: Ensure `blank_states_img.gif` is in the same directory as the script
- **CSV file not found**: Verify `50_states.csv` is in the correct location
- **Import errors**: Make sure pandas is installed: `pip install pandas`

## 🎉 Have Fun!

Challenge your friends, improve your geography skills, and see if you can name all 50 states!

---

**Built with Python 🐍 | Powered by Turtle Graphics 🐢**
