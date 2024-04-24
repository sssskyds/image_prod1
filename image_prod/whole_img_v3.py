import matplotlib
matplotlib.use('Agg')  # Use Agg backend for Google Colab
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Read data from text file
with open('figure_data.txt', 'r') as file:
    lines = file.readlines()
    figure_data_list = [list(map(float, line.strip().split())) for line in lines]

current_figure_index = 0

def update_figure(i):
    global current_figure_index, figure_data_list
    current_figure_data = figure_data_list[current_figure_index]
    im.set_array(current_figure_data)
    current_figure_index = (current_figure_index + 1) % len(figure_data_list)
    return [im]

# Create the initial plot
fig, ax = plt.subplots()
im = ax.imshow(figure_data_list[0], cmap='gray_r', vmin=0, vmax=1)

# Create the animation
ani = animation.FuncAnimation(fig, update_figure, frames=len(figure_data_list), interval=200, blit=True)

# Display the animation
from IPython.display import HTML
HTML(ani.to_jshtml())
