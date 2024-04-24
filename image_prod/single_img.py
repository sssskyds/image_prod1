import tkinter as tk

def create_pixel_grid(rows, cols, pixel_size, figure_data):
    root = tk.Tk()
    root.title("Pixel Grid")

    # Calculate the total size of the grid
    width = cols * pixel_size
    height = rows * pixel_size

    # Create a canvas to display the grid
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    # Draw the grid and fill in the figure data
    for row in range(rows):
        for col in range(cols):
            x1 = col * pixel_size
            y1 = row * pixel_size
            x2 = x1 + pixel_size
            y2 = y1 + pixel_size
            color = "black" if figure_data[row][col] else "white"
            # Change from create_rectangle to create_oval for circular pixels
            canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black" if figure_data[row][col] else "white")

    root.mainloop()

# Example usage:
# Define the figure data as a 2D matrix (list of lists) where True represents a filled pixel
figure_data1 =[[0, 0, 0, 0, 0, 0, 0.......], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.. ]...]

create_pixel_grid(rows=len(figure_data1), cols=len(figure_data1[0]), pixel_size=5, figure_data=figure_data1)
