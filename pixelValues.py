import cv2
import numpy as np
img = cv2.imread('me.jpg')

img[100,100] = [255,255,255]

for x in range(100):
    for y in range(100):
        img[x,y] = [0,0,0]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

