import numpy as np
import cv2
if __name__ == "__main__":

    cap = cv2.VideoCapture(0)

    fgbg = cv2.createBackgroundSubtractorMOG2(history=0, varThreshold=127, detectShadows=0)

    while(1):
        ret, frame = cap.read()

        fgmask = fgbg.apply(frame)

        cv2.imshow('frame', fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()