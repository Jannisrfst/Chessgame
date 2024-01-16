import tkinter as tk

root = tk.Tk()
root.title("Chessboard")

# Define the dimensions of the chessboard
width = 500
height = 500

# Create the canvas to draw the chessboard
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

# Draw the horizontal lines
for row in range(8):
    x0 = 0
    y0 = row * 62.5
    x1 = width
    y1 = y0
    canvas.create_line(x0, y0, x1, y1, fill="black")

# Draw the vertical lines
for col in range(8):
    x0 = col * 62.5
    y0 = 0
    x1 = x0
    y1 = height
    canvas.create_line(x0, y0, x1, y1, fill="black")

# Draw the alternating squares in black and white
square_size = 62.5
for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0:
            color = "white"
        else:
            color = "black"
        x0 = col * square_size
        y0 = row * square_size
        x1 = x0 + square_size
        y1 = y0 + square_size
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)

root.mainloop()
