import cv2

sourcePath ='watershed\waterShedTest.png'

source = cv2.imread(sourcePath)


gry = cv2.cvtColor(source,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gry, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)
threshBlur = cv2.GaussianBlur(thresh,(5,5),1)

def default():
    cv2.namedWindow('test')
    cv2.createTrackbar('hStrength','test',0,255,denoise)

    denoise(0)
    cv2.waitKey()



def denoise(blank):
    denoiseValue = cv2.getTrackbarPos('hStrength','test')
    denoised = cv2.fastNlMeansDenoising(threshBlur,denoiseValue,7,21)
    cv2.imshow('test',denoised)






default()
cv2.waitKey()

