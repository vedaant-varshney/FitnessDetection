import cv2 as cv
import numpy as np

img = cv.imread('images/Lionel-Messi.jpg')

cv.imshow("Messi", img)

def translate(img, x, y):
    translationMatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions= (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translationMatrix, dimensions)

# -x --> Left, -y --> Up, x --> Right, y --> Down

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    


translated = translate(img, 100, 200)

cv.imshow("Translated Messi", translated)

cv.waitKey(0)
cv.destroyAllWindows()