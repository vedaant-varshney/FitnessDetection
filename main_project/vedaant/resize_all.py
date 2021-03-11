# This is a placeholder file that will serve the purpose of resizing all of the images within each set

import os
import cv2
import numpy

curDir = os.getcwd()

set = "Set1"

path = os.path.join(curDir, "images", set, '1.png' )

img = cv2.imread(path)

cv2.imshow("Test",img )

cv2.waitKey(0)
cv2.destroyAllWindows()

dim = (100, 100)



# Assumes cwd is root
