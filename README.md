# Grid Path Visualization Tool

This interactive tool visualizes all possible paths from point O (0,0) to point M (n,m) in a rectangular grid, where movements are restricted to right (R) and up (U) directions only. It's particularly useful for understanding combinatorial path problems and visualizing different path possibilities in a grid.

## Features

- Interactive grid size selection (n × m dimensions)
- Visual representation of all possible paths
- Path selection dropdown to explore different routes
- Real-time display of total number of possible paths
- Clear visualization with start point (O) and end point (M)
- Grid lines for better orientation

## Prerequisites

- Python 3.8 or higher
- Jupyter Notebook
- Required Python packages (listed in `requirements.txt`)

## Installation

1. Clone or download this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open `path_visualization.ipynb`

3. Run all cells in the notebook

4. Interact with the visualization:
   - Use the 'n' dropdown to select the width of the grid
   - Use the 'm' dropdown to select the height of the grid
   - Use the 'Chemin' (Path) dropdown to select different paths
   - Observe the total number of possible paths displayed below

## How It Works

- The tool generates all possible paths using the concept of anagrams
- Each path is represented as a string of 'R' (right) and 'U' (up) movements
- For a grid of size n×m, each path will contain exactly n 'R' movements and m 'U' movements
- The total number of possible paths is calculated using combinatorial mathematics
- The visualization updates in real-time as you change parameters

## Mathematical Background

The number of possible paths in an n×m grid is given by the combination formula:
```
C(n+m, n) = (n+m)! / (n! * m!)
```
This represents the number of ways to arrange n 'R' moves and m 'U' moves in a sequence of n+m total moves.

## Files Description

- `path_grid_visualization.py`: Main implementation file containing all the functions and visualization logic
- `path_visualization.ipynb`: Jupyter notebook for running the visualization
- `requirements.txt`: List of Python package dependencies
- `README.md`: This file, containing documentation and instructions

## Dependencies

- ipywidgets: For interactive widgets
- matplotlib: For grid and path visualization
- numpy: For numerical operations
- IPython: For notebook interface and display features
