import numpy as np
import cv2
from matplotlib import pyplot as plt

if __name__ == "__main__":

    img = cv2.imread('/Users/udiram/Documents/GitHub/fitnessCV/Tutorials/images/Lionel-Messi.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(img,(x,y),3,255,-1)

    plt.imshow(img),plt.show()