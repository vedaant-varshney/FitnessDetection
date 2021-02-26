import cv2 as cv
import imutils
import numpy as np

cap = cv.VideoCapture(0)
prev = None
counter = 0

while True:
    ret, frame = cap.read()
    if ret:
        assert not isinstance(frame,type(None)), 'frame not found'

    frame = imutils.resize(frame, width=500)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = cv.GaussianBlur(frame, (25, 25), 0)

    if counter % 30 is 0:
        prev = frame
    counter = counter + 1
    cv.imshow('reference', prev)

    frDiff = cv.absdiff(frame, prev)
    thresh = cv.threshold(frDiff, 25, 255, cv.THRESH_BINARY)[1]
    #thresh = cv.dilate(thresh, None)
    cv.imshow('thresh', thresh)

    contours = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    xA = None
    yA = None
    xB = None
    yB = None
    for c in contours:
        (x, y, w, h) = cv.boundingRect(c)
        if xA is None:
            xA = x
            yA = y
            xB = x+w
            yB = y+h
        if x < xA:
            xA = x
        if x+w > xB:
            xB = x+w
        if y < yA:
            yA = y
        if y+h > yB:
            yB = y+h

        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    if xA is not None:
        cv.rectangle(frame, (xA, yA), (xB, yB),
                 (0, 255, 0), 2)

    cv.imshow('bounding', frame)

    cv.waitKey(0)
