import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("images/Lionel-Messi.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Creating Grayscale Histogram
# Note that we can create a histogram based on the mask of an image
gray_hist = cv2.calcHist([gray], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("Number of Pixels")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()


# Color Histogram
colors = ('b', 'g', 'r')

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Intensity")
plt.ylabel("Number of Pixels")

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()


cv2.waitKey(0)