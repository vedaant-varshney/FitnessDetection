import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":

    # load image
    img = cv2.imread("pics/EFFECTS.jpg")

    # convert to hsv
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # threshold using inRange
    range1 = (10, 20, 28)
    range2 = (255, 255, 255)
    mask = cv2.inRange(img, range1, range2)

    # apply morphology closing and opening to mask
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # make mask 3 channel
    mask = cv2.merge([mask, mask, mask])

    # invert mask
    mask_inv = 255 - mask

    # create white image for background
    white = np.full_like(img, (255, 255, 255))

    # apply mask to input
    img_masked = cv2.bitwise_and(img, mask)

    # apply inverted mask to white image
    white_masked = cv2.bitwise_and(white, mask_inv)

    # combine inverted mask with masked image
    result = cv2.add(img_masked, mask)

    # cv2.imshow('frame', result)

    # plt.imshow(img)
    # plt.show()
    # plt.imshow(img_masked)
    # plt.show()
    plt.imshow(mask)
    plt.show()

