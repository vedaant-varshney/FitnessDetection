import cv2
import os

curdir = os.getcwd()

file = os.path.join(curdir, 'main_project', 'vedaant', 'TestingVideoCrop', 'trimmedJJ.mp4')

cap = cv2.VideoCapture(file)


while True:
    ret, frame = cap.read()
    
    if ret == True:
        # (height, width) = frame.shape[:2]
        # print(frame.shape)

        isolated = frame[100:1000, 300:1600]
        cv2.imshow('Video', isolated)

        if cv2.waitKey(1) == 27:
            exit(0)

    else: 
        break