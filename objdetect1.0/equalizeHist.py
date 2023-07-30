import cv2

original = cv2.imread('cannyTest.png')
source = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
source = cv2.GaussianBlur(source,(3,3),1)


se = cv2.getStructuringElement(cv2.MORPH_RECT,(11,11))
background = cv2.morphologyEx(source, cv2.MORPH_DILATE,se)

source = cv2.divide(source,background,scale = 255)



clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))

source = clahe.apply(source)

cv2.imshow('l',source)
#source = cv2.equalizeHist(source)
cv2.imwrite('equalized.png',source)

contours = cv2.findContours(source,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]


finalContours = []
for k in contours:
    area = cv2.contourArea(k)
    finalContours.append((area,k))

finalContours.sort(key=lambda x : x[0], reverse = True)

cv2.drawContours(original,finalContours[0][1],-1,(0,0,255),3)
    

cv2.imshow('',source)
cv2.imshow('n',original)
cv2.waitKey()
