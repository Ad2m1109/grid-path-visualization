import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def anagrams(word):
    if len(word) < 2:
        yield word
    else:
        for i, letter in enumerate(word):
            if not letter in word[:i]:
                for j in anagrams(word[:i] + word[i + 1:]):
                    yield j + letter

def path_grid(n, m):
    pattern = 'R' * n + 'U' * m
    return [''.join(p) for p in anagrams(pattern)]

def afficher_grille(n, m, chemin, fig, ax):
    ax.clear()
    
    # Create grid
    for i in range(n + 1):
        ax.axhline(i, color='black', lw=0.5)
    for j in range(m + 1):
        ax.axvline(j, color='black', lw=0.5)

    # Set limits
    ax.set_xlim(-0.1, n + 0.1)
    ax.set_ylim(-0.1, m + 0.1)

    # Mark points O and M
    ax.text(-0.1, -0.2, 'O', fontsize=12, color='red', ha='center', va='center')
    ax.text(n + 0.1, m + 0.2, 'M', fontsize=12, color='blue', ha='center', va='center')

    # Remove axis ticks
    ax.set_xticks(np.arange(0, n + 1, 1))
    ax.set_yticks(np.arange(0, m + 1, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    # Draw path
    x, y = 0, 0
    for move in chemin:
        if move == 'R':
            ax.plot([x, x + 1], [y, y], 'g-', lw=2)
            x += 1
        elif move == 'U':
            ax.plot([x, x], [y, y + 1], 'g-', lw=2)
            y += 1

    ax.grid(True)
    ax.set_title(f"Grid {n}x{m} with path: {chemin}")
    canvas.draw()

def update_paths(*args):
    n = int(n_var.get())
    m = int(m_var.get())
    paths = path_grid(n, m)
    path_dropdown['values'] = paths
    path_var.set(paths[0] if paths else '')
    num_paths.set(f"Number of paths: {len(paths)}")
    if paths:
        afficher_grille(n, m, paths[0], fig, ax)

def on_path_change(*args):
    if path_var.get():
        n = int(n_var.get())
        m = int(m_var.get())
        afficher_grille(n, m, path_var.get(), fig, ax)

# Create main window
root = tk.Tk()
root.title("Grid Path Visualization")
root.geometry("800x600")

# Create frame for controls
control_frame = ttk.Frame(root, padding="10")
control_frame.pack(side=tk.LEFT, fill=tk.Y)

# Variables
n_var = tk.StringVar(value='2')
m_var = tk.StringVar(value='2')
path_var = tk.StringVar()
num_paths = tk.StringVar(value="Number of paths: 0")

# Create controls
ttk.Label(control_frame, text="Grid Configuration:").pack(pady=5)
ttk.Label(control_frame, text="n:").pack()
n_spinbox = ttk.Spinbox(control_frame, from_=1, to=6, textvariable=n_var, width=5)
n_spinbox.pack(pady=5)

ttk.Label(control_frame, text="m:").pack()
m_spinbox = ttk.Spinbox(control_frame, from_=1, to=6, textvariable=m_var, width=5)
m_spinbox.pack(pady=5)

ttk.Label(control_frame, text="Path:").pack(pady=5)
path_dropdown = ttk.Combobox(control_frame, textvariable=path_var, width=20)
path_dropdown.pack(pady=5)

ttk.Label(control_frame, textvariable=num_paths).pack(pady=5)

# Create matplotlib figure
fig, ax = plt.subplots(figsize=(6, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Bind events
n_var.trace('w', update_paths)
m_var.trace('w', update_paths)
path_var.trace('w', on_path_change)

# Initial update
update_paths()

# Start the application
root.mainloop()
