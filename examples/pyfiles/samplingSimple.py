import cv2
import numpy as np
from PIL import Image
from random import random, randrange

if __name__ == "__main__":
    # Opens the Video file
    cap = cv2.VideoCapture(0)
    i = 0
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        if i % 20 == 0:  # this is the line I added to make it only save one frame every 20
            cv2.imwrite('/Users/udiram/Documents/GitHub/FitnessDetection/examples/frames/frame' + str(i) + '.jpg', frame)
        i += 1

    cap.release()
    cv2.destroyAllWindows()