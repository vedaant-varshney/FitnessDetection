import cv2
import numpy as np

# Creates an array with 5 rows and 7 columns
test = np.zeros((5, 7))
print(test.shape)

print(test)

img = cv2.imread('images/Lionel-Messi.jpg')

print(img.shape)