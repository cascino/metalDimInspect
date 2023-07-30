'''
A simple program that lets users manually calibrate 
the threshold values used in the canny function
'''

import cv2


lowThresh = 0
highThresh = 0
midThresh = 0

sourcePath = 'diagnostics\\1.jpg'
windowName = 'test'

source = cv2.imread(sourcePath)
source = cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)

nameLow = 'd'
nameHigh = 'sigmaColor'
nameMid = 'sigmaSpace'


cv2.imshow('SourceImage',source)
cv2.waitKey()


def default():

   cv2.namedWindow(windowName)
   cv2.resizeWindow(windowName,800,800)

   cv2.createTrackbar(nameLow,windowName,0,200,cannyOnImage)
   cv2.createTrackbar(nameHigh,windowName,0,200,cannyOnImage)
   cv2.createTrackbar(nameMid,windowName,0,200,cannyOnImage)

   cannyOnImage(0)
   cv2.waitKey()


def cannyOnImage(blank):

   lowT = cv2.getTrackbarPos(nameLow, windowName)
   highT = cv2.getTrackbarPos(nameHigh,windowName)
   midT = cv2.getTrackbarPos(nameMid,windowName)

   cannyDst = cv2.bilateralFilter(source,lowT,highT,midT)
   cv2.imshow(windowName,cannyDst)
   cv2.resizeWindow(windowName,800,800)

default()


