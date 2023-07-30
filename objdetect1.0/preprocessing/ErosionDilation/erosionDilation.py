'''
A simple program that lets users calibrate erosion and
dilation kernels
'''
import cv2

sourcePath = 'erosionDilationTest.png'
windowName = 'test'

source = cv2.imread(sourcePath)
source = cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)
source = cv2.GaussianBlur(source,(5,5),1)

