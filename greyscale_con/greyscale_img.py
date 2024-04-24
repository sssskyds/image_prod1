import cv2
import numpy as np

# Read the original image
image = cv2.imread('C:\\Users\\ajeet\\OneDrive\\Desktop\\Elmos\\resize1\\frame1.png')
def extract_and_reconstruct_grayscale(image):
  """
  Extracts grayscale data from an image and displays the reconstructed grayscale image.

  Args:
      image (numpy.ndarray): The image data loaded using OpenCV.
  """

  # Convert the image to grayscale
  grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Reconstruct the grayscale image
  reconstructed_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2BGR)

  # Display the reconstructed image
  cv2.imshow("Grayscale Image", reconstructed_image)
  cv2.waitKey(0)  # Wait for a key press to close the window
  cv2.destroyAllWindows()

# Example usage
image_path = "color_image.jpg"
image = cv2.imread(image_path)

extract_and_reconstruct_grayscale(image)

print("Grayscale image displayed!")
