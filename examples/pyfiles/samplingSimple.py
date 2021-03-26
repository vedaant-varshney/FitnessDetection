import cv2
import numpy as np
from PIL import Image
from random import random, randrange

if __name__ == "__main__":
    # Opens the Video file
    cap = cv2.VideoCapture(0)
    frame_sampling_rate = randrange(3, 5)
    # frame_sampling_rate = 15
    print("frame sampling rate:")
    print(frame_sampling_rate)

    i = 0
    setNumber = 1
    imageNumber = 1

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == False:
            break

        if i % frame_sampling_rate == 0:  # this is the line I added to make it only save one frame every 'frame_sampling_rate'
            cv2.imwrite('/Users/udiram/Documents/GitHub/FitnessDetection/examples/frames/Set' + str(setNumber) + 'Image' + str(imageNumber) + '.jpg', frame)
            imageNumber += 1

        i += 1

        if imageNumber == 9:
            setNumber += 1
            imageNumber = 1






    cap.release()
    cv2.destroyAllWindows()