import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
if __name__ == "__main__":
    os.chdir('/Users/udiram/Documents/GitHub/FitnessDetection')
    curDir = os.getcwd()

    image_path = os.path.join(curDir, 'main_project', 'Udi', 'BackgroundExtract_udi')

    image_list = os.listdir(image_path)

    new_list = []
    previous = image_list[0].split('I')[0]
    temp_list = []

    for image in image_list:
        set_no = image.split('I')[0]
        if set_no == previous:
            temp_list.append(image)
            previous = set_no
        else:
            new_list.append(temp_list)
            temp_list = []
            temp_list.append(image)
            previous = set_no

    for i in range(0,3):
        print(i)

        new_dims = (20, 20)
        i = 1
    for image_set in new_list:

        full_array = np.zeros([20 * 8, 20])
        set_path = os.path.join(curDir, 'main_project', 'Udi', 'stacks', f'Set{i}.png')
        i += 1
        for value, image in enumerate(image_set):
            # print(value, image)

            img = cv2.imread(os.path.join(image_path, image))
            resized = cv2.resize(img, new_dims)
            resized = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            retval, binary = cv2.threshold(resized, 1, 255, cv2.THRESH_BINARY)

            lower_bound = value * 20
            upper_bound = ((value + 1) * 20)

            # plt.imshow(cv2.cvtColor(binary, cv2.COLOR_BGR2RGB))
            # plt.show()

            full_array[lower_bound:upper_bound, :] = binary

        # plt.imshow(full_array)
        # plt.show()
        print(full_array.shape)

        cv2.imwrite(set_path, full_array)