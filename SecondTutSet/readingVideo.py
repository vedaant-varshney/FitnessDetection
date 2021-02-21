import cv2 as cv

capture = cv.VideoCapture('images/output.avi')

while True:
    # returns the frame and a boolean representing if the frame was shown
    isTrue, frame = capture.read()
    cv.imshow('Video feed', frame)

    # breaks out of the loop if the letter d is pressed | kind of complicated reasons for why this works, dw about it too much
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


cv.waitKey(0)
cv.destroyAllWindows()