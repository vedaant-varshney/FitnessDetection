import cv2
import numpy as np

img = cv2.imread('images/Lionel-Messi.jpg')

cv2.imshow("Lionel Messi", img)

print(img.shape)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('blank', blank)

mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2 - 125), 150, 255, -1)
cv2.imshow('masking', mask)


masked_image = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('masked image', masked_image)

cv2.waitKey(0)
