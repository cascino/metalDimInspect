'''
A simple program that lets users manually calibrate thresholding
methods and values used in the threshold function
'''

import cv2



threshVal = 0
threshMax = 0
threshType = 0

sourcePath = 'Migrated\cannyTest.png'
windowName = 'test'

threshValName = 'Thresholding Value'
threshMaxName = 'Thresholding Maximum'
threshTypeName = 'Thresholding Type'

windowName = 'thresholdingTest'


source = cv2.imread(sourcePath)
cv2.imshow('bob',source)

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

