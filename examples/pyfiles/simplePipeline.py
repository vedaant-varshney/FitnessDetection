import binascii
from random import random, randrange

import cv
import cv2
import numpy as np
import scipy
from PIL import Image
from matplotlib import image, pyplot

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    i = 0
    frame_sampling_rate = randrange(3, 5)
    # frame_sampling_rate = 15
    print("frame sampling rate:")
    print(frame_sampling_rate)

    fgbg = cv2.createBackgroundSubtractorMOG2(history=0, varThreshold=127, detectShadows=0)

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == False:
            break
        if i % frame_sampling_rate == 0:  # this is the line I added to make it only save one frame every 20
            # cv2.imwrite('/Users/udiram/Documents/GitHub/FitnessDetection/examples/frames/frame' + str(i) + '.jpg', frame)
            cv2.imwrite('/Users/udiram/Documents/GitHub/FitnessDetection/examples/frames/frame.jpg', frame)

            sampled_frame = image.imread('/Users/udiram/Documents/GitHub/FitnessDetection/examples/frames/frame.jpg')
            # print(sampled_frame.shape)
            data = np.reshape([sampled_frame], (-1, 3))
            # print(data.shape)
            data = np.float32(data)

            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
            flags = cv2.KMEANS_RANDOM_CENTERS
            compactness, labels, centers = cv2.kmeans(data, 1, None, criteria, 10, flags)

            print('Dominant color is: bgr({})'.format(centers[0].astype(np.int32)))
            # ==========================================================================================
            hsv = cv2.cvtColor(sampled_frame, cv2.COLOR_BGR2HSV)

            lower_blue = np.array(centers[0].astype(np.int32))
            upper_blue = np.array(centers[0].astype(np.int32))

            print('below is blue low')
            print(lower_blue)

            mask = cv2.inRange(hsv, lower_blue, upper_blue)

            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(sampled_frame, sampled_frame, mask=mask)

            binary_img = cv2.inRange(hsv, lower_blue, upper_blue)

        i += 1

#fix issues here with img saving as black jpegs as well as not showing in cv2.imshow


    cap.release()
    cv2.destroyAllWindows()
