import cv2
import numpy as np
from PIL import Image
from random import random, randrange

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    i = 0
    frame_sampling_rate = randrange(3, 5)
    print("frame sampling rate:")
    print(frame_sampling_rate)


    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break


        if i % frame_sampling_rate == 0:  # this is the line I added to make it only save one frame every 20
            cv2.imwrite('/Users/udiram/Documents/GitHub/FitnessDetection/examples/frames/'+'frame.jpg', frame)