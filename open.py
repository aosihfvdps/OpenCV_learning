import cv2 as cv
from rescale import rescaleFrame, changeRes
    
    
img1 = cv.imread('img/26HWKLFGSUI6ZBRIHWSPVD4HCQ.jpg')

cv.imshow('cat', img1)


resized_image = rescaleFrame(img1, scale = 0.2)
cv.imshow('resized_cat', resized_image)
cv.waitKey(0)


#Capturing video
capture = cv.VideoCapture("videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, scale = 0.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()



#cv.waitKey(0)

