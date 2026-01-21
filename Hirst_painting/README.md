# Hirst Painting (Turtle)

A small Python script that recreates a Damien Hirst-style dot painting using the standard `turtle` module. It draws a 10×10 grid of colored dots on screen and closes when you click the window.

## Requirements
- Python 3.8+
- Standard library only (uses `turtle` and `random`)

## How to Run
1. Open a terminal and switch into this folder:
   ```bash
   cd Hirst_painting
   ```
2. Run the script:
   ```bash
   python painting.py
   ```
3. A Turtle graphics window opens; click the window to exit when the drawing finishes.

## What the Script Does
- Sets up a turtle, moves to the starting corner, and iterates through `number_of_dots`.
- For each dot it picks a random color from `color_list`, draws a 20px dot, and steps forward to lay out a grid.
- Every 10 dots it shifts up a row and returns to the left to start the next row.

## Customization
- Change `number_of_dots` to adjust total dots (grid is 10 columns by default; e.g., 100 → 10×10).
- Edit `color_list` to use your own palette of RGB tuples (0–255).
- Tweak the dot size in `tim.dot(20, ...)` and spacing in `tim.forward(50)` to alter scale and density.

## Notes
- Uses `my_screen.exitonclick()` so the window stays open until you click.
- If the canvas looks clipped, enlarge the Turtle window or reduce dot/spacing values.
