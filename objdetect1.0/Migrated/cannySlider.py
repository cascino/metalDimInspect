'''
A simple program that lets users manually calibrate 
the threshold values used in the canny function
'''

import cv2


lowThresh = 0
highThresh = 0

sourcePath = 'Migrated\\fc2_save_2023-07-24-101307-0014.jpg_2023-07-24-110340-0018.jpg'
windowName = 'test'

source = cv2.imread(sourcePath)
source = cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)
source = cv2.GaussianBlur(source,(9,9),6)
claheObject = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(3,2))
claheObject.apply(source)

nameLow = 'Low Threshold'
nameHigh = 'High threshold'
finalThresh = [0,0]

cv2.imshow('SourceImage',source)
cv2.waitKey()


def default():

   cv2.namedWindow(windowName)
   cv2.resizeWindow(windowName,800,800)

   cv2.createTrackbar(nameLow,windowName,0,200,cannyOnImage)
   cv2.createTrackbar(nameHigh,windowName,0,200,cannyOnImage)

   cannyOnImage(0)
   cv2.waitKey()


def cannyOnImage(blank):

   lowT = cv2.getTrackbarPos(nameLow, windowName)
   highT = cv2.getTrackbarPos(nameHigh,windowName)

   cannyDst = cv2.Canny(source,lowT,highT)
   cv2.imshow(windowName,cannyDst)
   finalThresh[0],finalThresh[1]= lowT,highT

default()
cv2.imwrite('cannyDst1.png',cv2.Canny(source,finalThresh[0],finalThresh[1]))

