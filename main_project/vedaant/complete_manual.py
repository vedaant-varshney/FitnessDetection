import os 
import numpy as np
import cv2
import sys

# Assumes that you are working in root directory
curDir = os.getcwd()

path = os.path.join(curDir, "images", "Set1")

file_list = os.listdir(path)

# Just a number that should be at the most extended part of the workout
primary = file_list[3]

if not os.path.exists(os.path.join(path, "Processed")):
    os.mkdir((os.path.join(path, "Processed")))
# Function serves to create a box and deliver coords of a user controlled rectangle
# Left click to begin drawing, drag to increase size, and unpress key to complete the rectangle
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
        coords = [initial_x, initial_y, x-initial_x]
        cv2.rectangle(img, (initial_x, initial_y), (initial_x+(x-initial_x), initial_y+(x-initial_x)), (0, 200, 0), thickness=5)


for img_name in file_list:
    img_path = os.path.join(path, img_name)
    img = cv2.imread(os.path.join(path, img_name))
    
    duplicate = img.copy()
    initial_x, initial_y = -1, -1
    coords = [-1, -1, -1]
    drawing = False

    cv2.namedWindow('Drawing')
    cv2.setMouseCallback("Drawing", create_box)

    while(1):
        cv2.imshow("Drawing", img)
        key = cv2.waitKey(1) & 0xFF
        complete = False
        if key==(ord('r')):
            img = duplicate.copy()
            coords = [-1, -1, -1]
        elif key ==(ord('e')):
            # row first, column second
            roi = img[coords[1]:coords[1]+coords[2], coords[0]:coords[0]+coords[2]]
            if roi.shape[0] != roi.shape[1]:
                print(coords)
                print(roi.shape)
                img = duplicate.copy()
            else:
                print(f"Completed Image {img_name}")
                cv2.imwrite((os.path.join(path, "Processed", img_name)), roi)
                
                font = cv2.FONT_HERSHEY_SIMPLEX
                org = (10, img.shape[0]-int(img.shape[0]*0.15))
                color = (200, 0, 0)
                thickness = 2
                fontScale = 1

                img = cv2.putText(img, "Saved... Press f to continue", org, font, fontScale, color, thickness, cv2.LINE_AA)

        elif key ==(ord('f')):
            break
        elif key == 27:
            cv2.destroyAllWindows()
            sys.exit(1)

    cv2.destroyAllWindows()

print("This code has been executed")

# duplicate = img.copy()


# for counter, file in enumerate(file_list):


# print(file_list)
