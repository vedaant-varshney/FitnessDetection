import numpy as np
import cv2
from matplotlib import pyplot as plt
#still doing that weird webcam thing...
if __name__ == "__main__":
    img = cv2.imread('pics/EFFECTS.jpg')
    cap = cv2.VideoCapture(0)

    while (1):
        ret, frame = cap.read()

    dimensions = frame.shape
    mask = np.zeros(frame.shape[:2], np.uint8)

    cv2.imshow('frame', result)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    height = frame.shape[0]
    width = frame.shape[1]
    channels = frame.shape[2]

    rect = (1000, 1000, 500, 500)  # change these for respective images
    cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    result = frame * mask2[:, :, np.newaxis]



    cv2.imshow('frame', result)
    plt.imshow(result)

    # plt.imshow(img)
    # plt.colorbar()
    # plt.show()
