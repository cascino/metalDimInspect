'''
A simple program that lets users manually calibrate thresholding
methods and values used in the threshold function
'''

import cv2
import numpy as np



threshVal = 0
threshMax = 0
threshType = 0

sourcePath = '2.jpg'
windowName = 'test'

threshValName = 'Thresholding Value'
threshMaxName = 'Thresholding Maximum'
threshTypeName = 'Thresholding Type'

windowName = 'thresholdingTest'


source = cv2.imread(sourcePath)
source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
source = cv2.GaussianBlur(source, (9,9),3)

clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(4,4))
source = clahe.apply(source )
clam = cv2.adaptiveThreshold(source, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,4)
kernel = np.ones((2,2), np.uint8)
clam = cv2.morphologyEx(clam, cv2.MORPH_OPEN, kernel)
kernel = np.ones((1,1), np.uint8)
clam = cv2.morphologyEx(clam, cv2.MORPH_CLOSE, kernel)
cv2.imshow('job',clam)
cv2.imwrite('clam.jpg',clam)
cv2.imshow('bob',source)
cv2.imwrite('bob.jpg',source)

def default():
    cv2.namedWindow(windowName)
    cv2.resizeWindow(windowName,800,800)

    cv2.createTrackbar(threshValName,windowName,0,255,thresholdOnImage)
    cv2.createTrackbar(threshMaxName,windowName,0,255,thresholdOnImage)
    cv2.createTrackbar(threshTypeName,windowName,0,4,thresholdOnImage)

    thresHoldingMethod(0)
    cv2.waitKey()



def thresHoldingMethod(type):
    d = [
        cv2.THRESH_BINARY,
        cv2.THRESH_BINARY_INV,
        cv2.THRESH_MASK,
        cv2.THRESH_TOZERO,
        cv2.THRESH_TRUNC
        ]
    return d[type]

def thresholdOnImage(blank):
    newThreshVal = cv2.getTrackbarPos(threshValName,windowName)
    newMaxVal = cv2.getTrackbarPos(threshMaxName,windowName)
    newThreshType = cv2.getTrackbarPos(threshTypeName,windowName)

    burner, thresh = cv2.threshold(source,newThreshVal,newMaxVal,thresHoldingMethod(newThreshType))
    cv2.imshow(windowName,thresh)
    
    

default()

