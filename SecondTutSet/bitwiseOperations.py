import cv2
import os
import numpy as np


blank = np.zeros((400, 400), dtype="uint8")

# the last value of -1 means the image is filled
rectangle = cv2.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)

cv2.imshow("Rectangle", rectangle)
cv2.imshow("circle", circle)

# Bitwise AND --> Returned the intersection of the two images 
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("Bitwise And", bitwise_and)

# Bitwise OR --> Returns both the intersection and the non-intersecting parts of the images
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Bitwise Or", bitwise_or)

# Bitwise XOR --> Returns the non-intersecting regions (with non-zero values)
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Bitwise Xor", bitwise_xor)

# Bitwise NOT --> Inverts the binary color
bitwise_not = cv2.bitwise_not(rectangle)
cv2.imshow("Bitwise Not", bitwise_not)



cv2.waitKey(0)