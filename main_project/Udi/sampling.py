import time

import cv2
import numpy as np
from PIL import Image
from random import random, randrange

if __name__ == "__main__":
    # Opens the Video file
    cap = cv2.VideoCapture('/Users/udiram/Documents/GitHub/FitnessDetection/main_project/Udi/input/trimmedJJ.mp4')
    frame_sampling_rate = randrange(3, 5)
    # frame_sampling_rate = 15
    print("frame sampling rate:")
    print(frame_sampling_rate)

    i = 0
    setNumber = 1
    imageNumber = 1

    while (cap.isOpened()):

        ret, frame = cap.read()

        # frame = cv2.resize(frame,(244,244),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)

        frame = frame[140:940, 560:1360]

        scale_percent = 30.5

        # calculate the 50 percent of original dimensions
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)

        # dsize
        dsize = (width, height)

        # resize image
        output = cv2.resize(frame, dsize)
        # cv2.imshow('Video', sky)

        if ret == False:
            break
        if i % frame_sampling_rate == 0:  # this is the line I added to make it only save one frame every 'frame_sampling_rate'
            # frame = cv2.resize(frame, (224, 224))
            cv2.imwrite('/Users/udiram/Documents/GitHub/FitnessDetection/main_project/Udi/UdiProcessed_test/Set' + str(
                setNumber) + 'Image' + str(imageNumber) + '.png', output)
            imageNumber += 1

        i += 1

        if imageNumber == 9:
            setNumber += 1
            imageNumber = 1

        cv2.imshow('example', ret)

    cap.release()
    cv2.destroyAllWindows()
