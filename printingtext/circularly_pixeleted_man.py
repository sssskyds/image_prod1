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
            color = "black" if figure_data.get((row, col), False) else "white"
            # Change from create_rectangle to create_oval for circular pixels
            canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

    root.mainloop()

# Example usage:
# Define the figure data as a dictionary with (row, col) as keys and True as values where the figure should appear
figure_data = {
    (0, 0): False, (0, 1): False, (0, 2): False, (0, 3): False, (0, 4): False, (0, 5): False, (0, 6): False,
    (0, 7): False, (0, 8): False, (0, 9): False, (0, 10): False, (0, 11): False, (0, 12): False, (0, 13): False,
    (0, 14): False, (0, 15): False, (0, 16): False, (0, 17): False, (0, 18): False, (0, 19): False, (1, 0): False,
    (1, 1): False, (1, 2): False, (1, 3): False, (1, 4): False, (1, 5): False, (1, 6): False, (1, 7): True,
    (1, 8): True, (1, 9): True, (1, 10): True, (1, 11): True, (1, 12): False, (1, 13): False, (1, 14): False,
    (1, 15): False, (1, 16): False, (1, 17): False, (1, 18): False, (1, 19): False, (2, 0): False, (2, 1): False,
    (2, 2): False, (2, 3): False, (2, 4): False, (2, 5): False, (2, 6): False, (2, 7): True, (2, 8): True, (2, 9): True,
    (2, 10): True, (2, 11): True, (2, 12): True, (2, 13): False, (2, 14): False, (2, 15): False, (2, 16): False,
    (2, 17): False, (2, 18): False, (2, 19): False, (3, 0): False, (3, 1): False, (3, 2): False, (3, 3): False,
    (3, 4): False, (3, 5): False, (3, 6): False, (3, 7): True, (3, 8): True, (3, 9): True, (3, 10): True, (3, 11): True,
    (3, 12): False, (3, 13): False, (3, 14): False, (3, 15): False, (3, 16): False, (3, 17): False, (3, 18): False,
    (3, 19): False, (4, 0): False, (4, 1): False, (4, 2): False, (4, 3): False, (4, 4): False, (4, 5): False,
    (4, 6): False, (4, 7): False, (4, 8): True, (4, 9): True, (4, 10): True, (4, 11): False, (4, 12): False,
    (4, 13): False, (4, 14): False, (4, 15): False, (4, 16): False, (4, 17): False, (4, 18): False, (4, 19): False,
    (5, 0): False, (5, 1): False, (5, 2): False, (5, 3): False, (5, 4): False, (5, 5): False, (5, 6): False,
    (5, 7): True, (5, 8): True, (5, 9): True, (5, 10): True, (5, 11): True, (5, 12): False, (5, 13): False,
    (5, 14): False, (5, 15): False, (5, 16): False, (5, 17): False, (5, 18): False, (5, 19): False, (6, 0): False,
    (6, 1): False, (6, 2): False, (6, 3): False, (6, 4): False, (6, 5): True, (6, 6): True, (6, 7): True, (6, 8): True,
    (6, 9): True, (6, 10): True, (6, 11): True, (6, 12): True, (6, 13): True, (6, 14): False, (6, 15): False,
    (6, 16): False, (6, 17): False, (6, 18): False, (6, 19): False, (7, 0): False, (7, 1): False, (7, 2): False,
    (7, 3): False, (7, 4): True, (7, 5): True, (7, 6): True, (7, 7): False, (7, 8): False, (7, 9): True, (7, 10): True,
    (7, 11): False, (7, 12): True, (7, 13): True, (7, 14): True, (7, 15): False, (7, 16): False, (7, 17): False,
    (7, 18): False, (7, 19): False, (8, 0): False, (8, 1): False, (8, 2): False, (8, 3): True, (8, 4): True,
    (8, 5): True, (8, 6): False, (8, 7): False, (8, 8): False, (8, 9): True, (8, 10): True, (8, 11): False,
    (8, 12): False, (8, 13): False, (8, 14): True, (8, 15): True, (8, 16): True, (8, 17): False, (8, 18): False,
    (8, 19): False, (9, 0): False, (9, 1): False, (9, 2): True, (9, 3): True, (9, 4): True, (9, 5): False,
    (9, 6): False, (9, 7): False, (9, 8): False, (9, 9): True, (9, 10): True, (9, 11): False, (9, 12): False,
    (9, 13): False, (9, 14): False, (9, 15): True, (9, 16): True, (9, 17): True, (9, 18): False, (9, 19): False,
    (10, 0): False, (10, 1): True, (10, 2): True, (10, 3): True, (10, 4): False, (10, 5): False, (10, 6): False,
    (10, 7): False, (10, 8): False, (10, 9): True, (10, 10): True, (10, 11): False, (10, 12): False, (10, 13): False,
    (10, 14): False, (10, 15): False, (10, 16): True, (10, 17): True, (10, 18): False, (10, 19): False, (11, 0): False,
    (11, 1): False, (11, 2): False, (11, 3): False, (11, 4): False, (11, 5): False, (11, 6): False, (11, 7): False,
    (11, 8): True, (11, 9): True, (11, 10): True, (11, 11): False, (11, 12): False, (11, 13): False, (11, 14): False,
    (11, 15): False, (11, 16): False, (11, 17): False, (11, 18): False, (11, 19): False, (12, 0): False, (12, 1): False,
    (12, 2): False, (12, 3): False, (12, 4): False, (12, 5): False, (12, 6): False, (12, 7): True, (12, 8): True,
    (12, 9): True, (12, 10): True, (12, 11): True, (12, 12): False, (12, 13): False, (12, 14): False, (12, 15): False,
    (12, 16): False, (12, 17): False, (12, 18): False, (12, 19): False, (13, 0): False, (13, 1): False, (13, 2): False,
    (13, 3): False, (13, 4): False, (13, 5): False, (13, 6): True, (13, 7): True, (13, 8): True, (13, 9): False,
    (13, 10): True, (13, 11): True, (13, 12): True, (13, 13): False, (13, 14): False, (13, 15): False, (13, 16): False,
    (13, 17): False, (13, 18): False, (13, 19): False, (14, 0): False, (14, 1): False, (14, 2): False, (14, 3): False,
    (14, 4): False, (14, 5): False, (14, 6): True, (14, 7): True, (14, 8): False, (14, 9): False, (14, 10): False,
    (14, 11): True, (14, 12): True, (14, 13): False, (14, 14): False, (14, 15): False, (14, 16): False, (14, 17): False,
    (14, 18): False, (14, 19): False, (15, 0): False, (15, 1): False, (15, 2): False, (15, 3): False, (15, 4): False,
    (15, 5): True, (15, 6): True, (15, 7): False, (15, 8): False, (15, 9): False, (15, 10): False, (15, 11): False,
    (15, 12): True, (15, 13): True, (15, 14): False, (15, 15): False, (15, 16): False, (15, 17): False, (15, 18): False,
    (15, 19): False, (16, 0): False, (16, 1): False, (16, 2): False, (16, 3): False, (16, 4): True, (16, 5): True,
    (16, 6): True, (16, 7): False, (16, 8): False, (16, 9): False, (16, 10): False, (16, 11): False, (16, 12): True,
    (16, 13): True, (16, 14): True, (16, 15): False, (16, 16): False, (16, 17): False, (16, 18): False, (16, 19): False,
    (17, 0): False, (17, 1): False, (17, 2): False, (17, 3): False, (17, 4): True, (17, 5): True, (17, 6): False,
    (17, 7): False, (17, 8): False, (17, 9): False, (17, 10): False, (17, 11): False, (17, 12): False, (17, 13): True,
    (17, 14): True, (17, 15): False, (17, 16): False, (17, 17): False, (17, 18): False, (17, 19): False, (18, 0): False,
    (18, 1): False, (18, 2): False, (18, 3): True, (18, 4): True, (18, 5): False, (18, 6): False, (18, 7): False,
    (18, 8): False, (18, 9): False, (18, 10): False, (18, 11): False, (18, 12): False, (18, 13): False, (18, 14): True,
    (18, 15): True, (18, 16): False, (18, 17): False, (18, 18): False, (18, 19): False, (19, 0): False, (19, 1): False,
    (19, 2): False, (19, 3): True, (19, 4): True, (19, 5): False, (19, 6): False, (19, 7): False, (19, 8): False,
    (19, 9): False, (19, 10): False, (19, 11): False, (19, 12): False, (19, 13): False, (19, 14): False, (19, 15): True,
    (19, 16): False, (19, 17): False, (19, 18): False, (19, 19): False, (20, 0): False, (20, 1): False, (20, 2): False,
    (20, 3): False, (20, 4): False, (20, 5): False, (20, 6): False, (20, 7): False, (20, 8): False, (20, 9): False,
    (20, 10): False, (20, 11): False, (20, 12): False, (20, 13): False, (20, 14): False, (20, 15): False,
    (20, 16): False, (20, 17): False, (20, 18): False, (20, 19): False, (21, 0): False, (21, 1): False, (21, 2): False,
    (21, 3): False, (21, 4): False, (21, 5): False, (21, 6): False, (21, 7): False, (21, 8): False, (21, 9): False,
    (21, 10): False, (21, 11): False, (21, 12): False, (21, 13): False, (21, 14): False, (21, 15): False,
    (21, 16): False, (21, 17): False, (21, 18): False, (21, 19): False}


create_pixel_grid(rows=20, cols=20, pixel_size=20, figure_data=figure_data)
