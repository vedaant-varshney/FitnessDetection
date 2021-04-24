import cv2
import numpy as np

messi = cv2.imread('images/Lionel-Messi.jpg')
messi_slice = cv2.imread('images/MessiSlice.jpg')

messi_gray = cv2.cvtColor(messi, cv2.COLOR_BGR2GRAY)
messi_slice_gray = cv2.cvtColor((messi_slice), cv2.COLOR_BGR2GRAY)

w, h = messi_slice_gray.shape[::-1]

print(w, h)

res = cv2.matchTemplate(messi_gray, messi_slice_gray, cv2.TM_CCOEFF_NORMED)

threshold = 0.9
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(messi, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)

cv2.imshow('dtected', messi)

print(messi.shape)

# I just created a slice of the original image to refer to later
# messi_roi = messi[ 200:300, 300:400]
# cv2.imwrite('images/MessiSlice.jpg', messi_roi)





cv2.waitKey(0)
