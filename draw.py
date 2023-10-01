import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)


blank[200:300, 300:400] = 0,0,255
cv.imshow("green", blank)

# img1 = cv.imread('img/cat.jpg')

# img1[200:300, 300:400] = 0,0,255
# cv.imshow("green", img1)

cv.waitKey(0)