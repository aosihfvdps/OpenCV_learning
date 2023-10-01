import cv2 as cv

def rescaleFrame(frame, scale=0.75): #Images, videos, Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height): #Only Live video
    capture.set(3, width)
    capture.set(4, height)