import tkinter as tk

def create_pixel_grid(rows, cols, pixel_size):
    root = tk.Tk()
    root.title("Pixel Grid")

    # Calculate the total size of the grid
    width = cols * pixel_size
    height = rows * pixel_size

    # Create a canvas to display the grid
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    # Draw the grid
    for row in range(rows):
        for col in range(cols):
            x1 = col * pixel_size
            y1 = row * pixel_size
            x2 = x1 + pixel_size
            y2 = y1 + pixel_size
            canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")

    root.mainloop()

# Example usage:
create_pixel_grid(rows=128, cols=64, pixel_size=10)
