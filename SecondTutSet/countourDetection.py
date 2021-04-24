import cv2
import numpy as np

img = cv2.imread("images/Lionel-Messi.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow("Blank image", blank)

# Blurring the image can reduce the number of contours in the image
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)


canny = cv2.Canny(blur, 125, 175)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Edges", canny)

# Using thresholding can change how contouring works
ret, thresh = cv2.threshold(blur, 125, 255, cv2.THRESH_BINARY)
cv2.imshow("thresholded image", thresh)


# Looks at the edges of the image and returns the 
# countours: List of all the countours in the image
# heirarchies: representation of the countours 
# cv2.RETR_LIST returns all the contours in the image, cv2.RETR_EXTERNAL for external countours, and cv2.RETR_TREE all the heirarchical countours
# cv2.CHAIN_APPROX_NONE is the contour approximation method. cv2.CHAIN_APPROX_SIMPLE simplifies the contours through compression
contours, heirarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# prints the numbers of contours found

print(len(contours))

cv2.drawContours(blank, contours, -1, (200, 100, 0), 1)

cv2.imshow('Contours Drawn', blank)

cv2.waitKey(0)