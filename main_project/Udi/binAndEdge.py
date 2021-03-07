import cv2
import numpy as np
from PIL import Image

if __name__ == "__main__":
    ogImage = Image.open("/Users/udiram/Documents/GitHub/FitnessDetection/examples/pics/crop1.jpg")


    ogImage = ogImage.convert('L')
    im = np.array(ogImage)

    im = np.uint8(im)

    im = cv2.bitwise_not(im)

    # im = np.log10(im)
    maxim = np.max(im)
    minim = np.min(im)
    thresh = maxim - minim
    print(str(thresh))
    # im = (im > thresh / 4.27) * 255
    blur = cv2.GaussianBlur(im, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # im_bin_64 = (im > thresh / 2.55) * 255  # make this not a hardcoded value, to accomodate all images
    # im_bin_64 = (im > 57) * 255
    # calculate max and min vals of the image, then thresh val is x/2
    # print(im_bin_64)

    im_bin = np.concatenate((th3,), axis=1)
    testImage = Image.fromarray(np.uint8(im_bin))
    width, height = testImage.size  # Get dimensions
    # testImage = testImage.crop((0, 100, width, (height / 2) - 125))

    testImage.save('/Users/udiram/Documents/GitHub/FitnessDetection/examples/pics/bandw1.png')

    img = cv2.imread('/examples/pics/bandw.png')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    n_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresh)

    # print(n_labels)


    # this needs to be big enough to accomodate for all values, so based on number of crops, rn, ionly one entry accepted

    size_thresh = 1
    for i in range(1, n_labels):
        if stats[
            i, cv2.CC_STAT_AREA] >= size_thresh:  # look into docs, why do we have an if statement here?
            # print(stats[i, cv2.CC_STAT_AREA])
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=1)

            # result = Image.fromarray(ogImage)
            result = ogImage.crop((x, y, x + w, y + h))

            if 10000 < w * h:  # > 30: gotta make the 100 value variable ask seb
                result.save("/Users/udiram/Documents/GitHub/FitnessDetection/examples/pics/crop" + str(i) + ".jpg")
                # columnList.append((x, x + w))
                # LadderReduce.ladderReduce(result, x, w)
        # print(columnList)
        cv2.imwrite("/examples/pics/out.png", img)
