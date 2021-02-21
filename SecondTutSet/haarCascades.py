import cv2

img = cv2.imread("images/Lionel-Messi.jpg")
cv2.imshow("Lionel Messi", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Messi", gray)


haar_cascade = cv2.CascadeClassifier('SecondTutSet/haarFace.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# Number of faces found
print(len(faces_rect))

# Coordinates of rectangle for the first face
print(faces_rect)

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), thickness=2)

cv2.imshow("detected faces", img)

cv2.waitKey(0)


