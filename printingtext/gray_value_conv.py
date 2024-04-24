import cv2
import matplotlib.pyplot as plt

# Read the original image
image = cv2.imread('C:\\Users\\ajeet\\OneDrive\\Pictures\\head-roll.png')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image using Matplotlib
plt.imshow(gray_image, cmap='gray')
plt.show()
