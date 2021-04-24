import os 
import numpy as np
import cv2
import sys

if __name__ == "__main__":

    # Assumes that you are working in root directory
    

    # Check current working directory.
    retval = os.getcwd()
    print("Current working directory %s" % retval)

    # Remove this path 
    # path = '../../'

    # Now change the directory
    # os.chdir(path)

    # Check current working directory.
    retval = os.getcwd()

    print ("Directory changed successfully %s" % retval)

    correct = input("Is this the correct directory? (Write false is not so) ")

    if correct == "false":
        sys.exit(1)
    else:
        print("Moving on")


    set_number_start = int(input("Set number start point "))
    set_number_end = int(input("Set number end point "))

    for set_number in range(set_number_start, set_number_end+1):

        path = os.path.join(retval, "images", "Set"+str(set_number))
        print(path)

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


        img_path = os.path.join(path, primary)
        img = cv2.imread(img_path)

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
                roi = img[coords[1]:coords[1]+coords[2], coords[0]:coords[0]+coords[2]]
                if roi.shape[0] != roi.shape[1]:
                    print(coords)
                    print(roi.shape)
                    img = duplicate.copy()
                else:
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

        for img_name in file_list:
            current_path = os.path.join(path, img_name)
            new_path = os.path.join(path, "Processed", img_name)
            img2process = cv2.imread(current_path)
            
            if img2process is not None or []:
                roi = img2process[coords[1]:coords[1]+coords[2], coords[0]:coords[0]+coords[2]]
                cv2.imwrite((os.path.join(path, "Processed", img_name)), roi)
                print(f"{img_name} has been processed in set {str(set_number)}")

            cv2.destroyAllWindows()

        print(f"This code has been executed for Set {str(set_number)}")



    # duplicate = img.copy()


    # for counter, file in enumerate(file_list):


    # print(file_list)
