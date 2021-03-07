import cv2
import numpy as np

if __name__ == "__main__":

    # load image
    img = cv2.imread("pics/dog.jpg")
    cap = cv2.VideoCapture(0)
    while (1):
        ret, frame = cap.read()

        # convert to hsv
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # threshold using inRange
        range1 = (50, 50, 50)
        range2 = (255, 255, 255)
        mask = cv2.inRange(hsv, range1, range2)

        # apply morphology closing and opening to mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # make mask 3 channel
        mask = cv2.merge([mask, mask, mask])

        # invert mask
        mask_inv = 255 - mask

        # create white image for background
        white = np.full_like(frame, (255, 255, 255))

        # apply mask to input
        img_masked = cv2.bitwise_and(frame, mask)

        # apply inverted mask to white image
        white_masked = cv2.bitwise_and(white, mask_inv)

        # combine inverted mask with masked image
        result = cv2.add(img_masked, mask)

        cv2.imshow('frame', mask)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
