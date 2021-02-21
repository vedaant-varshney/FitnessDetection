import cv2 as cv
import os

print(os.getcwd())

img = cv.imread('images/Lionel-Messi.jpg')



print(img.shape)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height) 

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)    

# cv.imshow('Lionel Messi Original Size', img)
# cv.imshow("Lionel Messi 75%",rescaleFrame(img))


video_feed = cv.VideoCapture(0)

while True:
    isTrue, frame = video_feed.read()
    frame_resized = rescaleFrame(frame, scale=0.5)

    cv.imshow('Full Size Webcam', frame)
    cv.imshow("75% Scaling", frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video_feed.release()
cv.destroyAllWindows()