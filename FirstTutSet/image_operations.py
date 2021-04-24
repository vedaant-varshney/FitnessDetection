import numpy as np
import cv2

img = cv2.imread('images/Lionel-Messi.jpg', cv2.IMREAD_COLOR)

px = img[200, 500]

print(px)

# Region of Image
ROI = img[100:150, 100:150]
print(ROI)

# We can place or save a part of an image in other locations
img[100:150, 100:150] = [255, 255, 255]




cv2.imshow("Messi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()