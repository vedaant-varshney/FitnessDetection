import cv2
import numpy as np
if __name__ == "__main__":

    img = cv2.imread('/Users/udiram/Documents/GitHub/fitnessCV/Tutorials/images/Lionel-Messi.jpg')
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    sift = cv2.SIFT()
    kp = sift.detect(gray,None)

    img=cv2.drawKeypoints(gray,kp)

    cv2.imwrite('sift_keypoints.jpg',img)