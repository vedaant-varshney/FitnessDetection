import os 
import numpy as np
import cv2

# Assumes that you are working in root directory
curDir = os.getcwd()

path = os.path.join(curDir, "images", "Set1")

file_list = os.listdir(path)

# Just a number that should be at the most extended part of the workout
primary = file_list[3]

img = cv2.imread(os.path.join(path, primary))

cv2.imshow("Test", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


# duplicate = img.copy()


# for counter, file in enumerate(file_list):


# print(file_list)
