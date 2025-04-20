import tkinter as tk

def create_grid(canvas, rows, cols, cell_size):
    """Create a grid of blue rectangles on the canvas."""
    for row in range(rows):
        for col in range(cols):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black", tags="cell")

def on_eraser_drag(event):
    """Handle the eraser drag event and turn cells white."""
    x, y = event.x, event.y
    overlapping_items = canvas.find_overlapping(x, y, x + eraser_size, y + eraser_size)
    for item in overlapping_items:
        canvas.itemconfig(item, fill="white")

def move_eraser(event):
    """Move the eraser rectangle to follow the cursor."""
    x, y = event.x, event.y
    canvas.coords(eraser, x, y, x + eraser_size, y + eraser_size)
    on_eraser_drag(event)

# Parameters
cell_size = 20
rows = 20
cols = 20
eraser_size = 40

# Initialize Tkinter window
root = tk.Tk()
root.title("Canvas Eraser")

# Create canvas
canvas_width = cols * cell_size
canvas_height = rows * cell_size
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Create the grid
create_grid(canvas, rows, cols, cell_size)

# Create the eraser rectangle
eraser = canvas.create_rectangle(0, 0, eraser_size, eraser_size, fill="gray", outline="black", tags="eraser")

# Bind mouse events
canvas.bind("<B1-Motion>", move_eraser)

# Start the Tkinter event loop
root.mainloop()
