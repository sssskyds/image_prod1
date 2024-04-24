import cv2
import numpy as np

# Read the original image
image = cv2.imread('C:\\Users\\ajeet\\OneDrive\\Desktop\\Elmos\\Untitled\\frame6.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image: 0 is black, 255 is white
_, thresholded = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Create the stick_figure_data dictionary
stick_figure_data = {}

# Iterate over the image
for y in range(thresholded.shape[0]):
    for x in range(thresholded.shape[1]):
        # If the pixel is black (part of the stick figure), set the value in the dictionary to True
        stick_figure_data[(x, y)] = thresholded[y, x] == 0

print(stick_figure_data)
