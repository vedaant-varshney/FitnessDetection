import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h,s,v = 100,100,100

# Creating track bar
cv2.createTrackbar('Lower Range H', 'result',0,179,nothing)
cv2.createTrackbar('Lower Range S', 'result',0,255,nothing)
cv2.createTrackbar('Lower Range V', 'result',0,255,nothing)

cv2.createTrackbar('Upper Range H', 'result',0,179,nothing)
cv2.createTrackbar('Upper Range S', 'result',0,255,nothing)
cv2.createTrackbar('Upper Range V', 'result',0,255,nothing)

while(1):

    _, frame = cap.read()

    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    lower_h = cv2.getTrackbarPos('Lower Range H','result')
    lower_s = cv2.getTrackbarPos('Lower Range S','result')
    lower_v = cv2.getTrackbarPos('Lower Range V','result')

    # Set the lower bound to a range where it tracks about everything, and set uppers to the max value. 
    # Then, reduce them slowly until you get your range
    upper_h = cv2.getTrackbarPos('Upper Range H','result')
    upper_s = cv2.getTrackbarPos('Upper Range S','result')
    upper_v = cv2.getTrackbarPos('Upper Range V','result')

    # Normal masking algorithm
    lower_range = np.array([lower_h,lower_s,lower_v])
    upper_range = np.array([upper_h, upper_s, upper_v])

    mask = cv2.inRange(hsv,lower_range, upper_range)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()