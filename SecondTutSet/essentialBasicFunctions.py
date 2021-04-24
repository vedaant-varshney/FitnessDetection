import cv2 as cv

img = cv.imread('images/Lionel-Messi.jpg')

# Changing Color Space
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Adding Blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)

# Dilating Images
dilated = cv.dilate(canny, (7, 7), iterations=3)

# Eroding Images
eroded = cv.erode(dilated, (3, 3), iterations=1)

#Resize 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)

# For cropping, keep in mind that images are all just arrays of each other
cv.imshow('Test1', img)
cv.imshow('Test', resized)


cv.waitKey(0)
cv.destroyAllWindows()