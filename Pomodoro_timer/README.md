# Pomodoro Timer

A productivity timer application built with Python's Tkinter library, implementing the Pomodoro Technique to help you manage your time effectively.

## Features

- **25-minute work sessions** followed by short breaks
- **Short breaks (5 minutes)** after each work session
- **Long breaks (20 minutes)** after every 4 work sessions
- **Visual checkmarks** to track completed work sessions
- **Color-coded labels** to indicate current session type (Work/Break)
- **Simple Start/Reset controls**

## How It Works

The Pomodoro Technique is a time management method that uses a timer to break work into intervals:

1. Work for 25 minutes
2. Take a 5-minute short break
3. Repeat steps 1-2
4. After 4 work sessions, take a 20-minute long break

## Installation

1. Make sure you have Python installed on your system
2. Clone this repository or download the files
3. No additional dependencies required (uses built-in Tkinter)

```bash
python main.py
```

## Usage

1. Run the program
2. Click **Start** to begin a work session
3. The timer will automatically cycle through work and break periods
4. Click **Reset** to stop and reset the timer
5. Checkmarks (✅) appear after each completed work session

## Customization

You can customize the timer durations by modifying these constants in `main.py`:

```python
WORK_MIN = 25          # Work session duration (minutes)
SHORT_BREAK_MIN = 5    # Short break duration (minutes)
LONG_BREAK_MIN = 20    # Long break duration (minutes)
```

## Optional Enhancement

For the best experience, add a `tomato.png` image file to the Pomodoro_timer folder. The program will display the tomato image as part of the UI, but it will still work without it.

## Technologies Used

- Python
- Tkinter (GUI)

## License

This project is open source and available for personal and educational use.
