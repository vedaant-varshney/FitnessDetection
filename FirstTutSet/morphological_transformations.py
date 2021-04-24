import cv2
import numpy as np

cap = cv2.VideoCapture(1)

# Normalizes an hsv from [359, 100, 100] to [179, 255, 255]
def normalize(hsv_array):
    hsv_array[0] = (hsv_array[0] / 359) * 179
    hsv_array[1] = (hsv_array[1] / 100) * 255
    hsv_array[2] = (hsv_array[2] / 100) * 255

    return hsv_array


lower_red = np.array([84, 51, 43])
upper_red = np.array([106, 155, 255])

print(lower_red)
print(upper_red)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # hsv limits in opencv are 0-179 for hue, 0-255 for saturation and value
    

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # opening is removing false positives (stuff being detected that shouldn't be)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # closing is removing false negatives (stuff not being detected that should be)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Useful for future operations
    # tophat, difference between input and opening
    # blackhat, difference between closing and the input image

    
    # cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('frame', frame)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)





    # escape key
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
        
cv2.destroyAllWindows()
cap.release()