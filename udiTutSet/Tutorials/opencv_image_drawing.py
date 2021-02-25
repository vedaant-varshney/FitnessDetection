import numpy as np
import cv2

img = cv2.imread('images/Lionel-Messi.jpg', cv2.IMREAD_COLOR)

# Color format is BGR
cv2.line(img, (0, 0), (300, 300), (200, 0, 0), 10)

# top left then bottom right
cv2.rectangle(img, (15, 25), (500,160), (255, 255, 255), 5)

cv2.circle(img, (500, 500), 100, (0, 0, 0), 5)


pts = np.array([[20, 35], [20, 400], [250, 500], [300, 10]], np.int32)

# as many rows as it takes for a 1 row by 2 column array
pts = pts.reshape((-1, 1, 2))

cv2.polylines(img, [pts], True, (0, 255, 255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Lionel Messi", (0, 600), font, 1, (200, 255, 255), 2, cv2.LINE_AA)


cv2.imshow('Lionel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()