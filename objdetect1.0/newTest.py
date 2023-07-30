import cv2

sourcePath = 'cannyTest.png'

source = cv2.imread(sourcePath)
gray = cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),1)



se = cv2.getStructuringElement(cv2.MORPH_RECT, (8,8))
background = cv2.morphologyEx(blur, cv2.MORPH_DILATE,se)

beforeOut = cv2.divide(gray, background,scale = 255 )
cv2.imshow('beforeOut',beforeOut)

canny = cv2.Canny(blur, 75,95,-1)
dilate = cv2.dilate(canny,(5,5),iterations=4)
erode = cv2.erode(dilate,(5,5),iterations=2)
#cv2.imshow('canny',canny)
#cv2.waitKey()



contours, hierarchy = cv2.findContours(erode,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


finalContours = []
minArea = 500
for k in contours:
    area = cv2.contourArea(k)
    if area > minArea:
        finalContours.append((k,area))

finalContours.sort(key=lambda x : x[1],reverse=True )

for j in finalContours: 
    print(j[1])
cv2.drawContours(source,finalContours[0][0],-1,(0,0,255),2)
cv2.imshow('source',source)

cv2.imshow('canny',erode)

cv2.waitKey()