import numpy as np
import cv2

dimensions = (100,100)

#creation of array
l,w = dimensions
arr = []
for i in range(0, w):
  arr.append([])
  for j in range(0, l):
    arr[i].append(0)

#makes the rectangle
def rectangle(length, width):
  for i in range(0, width): 
    for j in range(0, length): 
      arr[i][j] = 255

#code for user
def rectangle_circle_creator ():
  creation = input("Do you want a circle or a rectangle? ")
  if creation == "circle":
    radius = input("Radius:")
  if creation == "rectangle":
    length = int(input ("Length: "))
    width = int(input("Width: "))
    rectangle(length, width)
    return arr


numpy_array = np.array(rectangle_circle_creator(), dtype=np.uint8)

cv2.imshow("Thuvaragan Display", numpy_array)


cv2.waitKey(0)
cv2.destroyAllWindows()

# rectangle_circle_creator()

