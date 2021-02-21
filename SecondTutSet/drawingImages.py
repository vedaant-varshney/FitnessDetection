import cv2 as cv
import numpy as np

img = cv.imread('images/Lionel-Messi.jpg')

blank = np.zeros((500, 500, 3), dtype='uint8')

# Paint the image a specific color
# blank[:] = 30, 0, 175
blank[200:300, 300:400] = 30, 0, 175


cv.imshow("Blank Square", blank)
cv.imshow("Lionel Messi", img)

cv.waitKey(0)
