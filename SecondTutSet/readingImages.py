import cv2 as cv
import os

print(os.getcwd())

# file path to the image
img = cv.imread('images/Lionel-Messi.jpg')

# name of frame and then the img requested
cv.imshow("Lionel Messi", img)

# if any key is pressed, exit out of the program
cv.waitKey(0)
cv.destroyAllWindows()