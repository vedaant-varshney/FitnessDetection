import cv2
import numpy as np
from IPython.utils import capture

if __name__ == "__main__":

    import numpy as np
    import cv2

    # file_path = "vid.mp4"

    cap = cv2.VideoCapture(0)

    first_iter = True
    result = None
    while True:
        ret, frame = cap.read()
        if frame is None:
            break

        if first_iter:
            avg = np.float32(frame)
            first_iter = False

        cv2.accumulateWeighted(frame, avg, 0.005)
        result = cv2.convertScaleAbs(avg)

    cv2.imshow('video bw', result)
    # cv2.imshow('video original', frame)
    cv2.imwrite('/Users/udiram/Documents/GitHub/FitnessDetection/examples/frames/fore.jpg', result)


    cv2.waitKey(0)

    capture.release()
    cv2.destroyAllWindows()