import os
import cv2
import numpy as np

# Just so i know where the starting point is
print(os.getcwd())

img = cv2.imread("images/Lionel-Messi.jpg")
duplicate = img.copy()

initial_x, initial_y = -1, -1
coords = [-1, -1, -1, -1]
drawing = False

def create_box(event, x, y, flags, param):
    global initial_x, initial_y, coords, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        initial_x, initial_y = x, y
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.line(img, (initial_x, initial_y), (initial_x, initial_y+(x-initial_x)), (0, 200, 0), thickness=3)
            cv2.line(img, (initial_x, initial_y), (x, initial_y), (0, 200, 0), thickness=3)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (initial_x, initial_y), (x, initial_y+(x-initial_x)), (0, 200, 0), thickness=5)
        coords = [initial_x, initial_y, x, initial_y+(x-initial_x)]
    
    

cv2.namedWindow('Drawing')
cv2.setMouseCallback("Drawing", create_box)

while(1):
    cv2.imshow("Drawing", img)
    key = cv2.waitKey(1) & 0xFF
    if key==(ord('r')):
        img = duplicate.copy()
        coords = [-1, -1, -1, -1]
    if key ==(ord('e')):
        roi = img[coords[0]:coords[2], coords[1]:coords[3]]
        print(roi.shape)
    
    elif key == 27:
        break

cv2.destroyAllWindows()