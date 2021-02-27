import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__ == "__main__":

    img = cv2.imread('pics/EFFECTS.jpg')

    dimensions = img.shape
    mask = np.zeros(img.shape[:2], np.uint8)

    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    height = img.shape[0]
    width = img.shape[1]
    channels = img.shape[2]

    rect = (1000, 1000, 500, 500)  # change these for respective images
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]

    plt.imshow(img)
    plt.colorbar()
    plt.show()