import tkinter as tk
from PIL import Image, ImageTk

def pixelate_image(image_path, rows=64, cols=128, pixel_size=10):
    # Load the image using PIL
    original_image = Image.open(image_path)
    # Resize the image to the desired grid size
    resized_image = original_image.resize((cols, rows), Image.NEAREST)

    # Create a tkinter window
    root = tk.Tk()
    root.title("Pixelated Image")

    # Create a canvas to display the pixelated image
    canvas = tk.Canvas(root, width=cols*pixel_size, height=rows*pixel_size)
    canvas.pack()

    # Convert the PIL image to a tkinter PhotoImage
    tk_image = ImageTk.PhotoImage(resized_image)

    # Create the pixelated grid
    for y in range(0, rows):
        for x in range(0, cols):
            # Get the color of the current pixel
            pixel_color = resized_image.getpixel((x, y))
            # Create a rectangle on the canvas with the pixel color
            canvas.create_rectangle(x*pixel_size, y*pixel_size, (x+1)*pixel_size, (y+1)*pixel_size, fill="white", outline="")

    root.mainloop()

# Example usage:
input_image_path = "C:\\Users\\ajeet\\OneDrive\\Pictures\\head-roll.png"
pixelate_image(input_image_path)
