import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # hsv limits
    lower_red = np.array([150, 150, 50])
    upper_red = np.array([180, 255, 150])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    # creating a kernel to smooth from, 225 is 15 x 15
    kernel = np.ones((15, 15), np.float32) / 225
    smoothed = cv2.filter2D(res, -1, kernel)

    # Gaussian Blur
    blur = cv2.GaussianBlur(res, (15, 15), 0)
    # Median blur
    median = cv2.medianBlur(res, 15)
    # bilateral blur
    bilat = cv2.bilateralFilter(res, 15, 75, 75)


    # cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow("median", median)
    cv2.imshow('bilateral', bilat)

    # escape key
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
        
cv2.destroyAllWindows()
cap.release()