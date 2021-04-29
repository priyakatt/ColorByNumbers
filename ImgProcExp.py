#
# ImgProcExp.py, Expanded imaging processing
#Load an image,segment image into color ranges using masks, find shapes from masks
#
import cv2
import numpy as np

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

print(rgb_to_hsv(255, 255, 255))
print(rgb_to_hsv(0, 215, 0))

image = cv2.imread('3Ust9Lq.png',1)     #load image

resize = cv2.resize(image, (320,240))   #resize to PiTFT screen size
hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)   #Conveert from BGR to HSV
color = image[10,10]    #test what color pixel 10,10 is
print(color)
light_red = np.array([0,200,200])   #Light red range
dark_red = np.array([0,255,255])    #Dark Red Range
light_blue =np.array ([94, 80, 2])  #Light Blue Range
dark_blue =np.array([126,255,255])  #Dark Blue Range
light_green=np.array([25,52,72])    #light Green Range
dark_green = np.array([102,255,255])    #Dark Green Range
maskRed = cv2.inRange(hsv_img, light_red, dark_red)     #red mask
maskBlue = cv2.inRange(hsv_img, light_blue, dark_blue)  #blue mask
maskGreen = cv2.inRange(hsv_img, light_green, dark_green)   #green mask
resultRed = cv2.bitwise_and(resize, resize, mask=maskRed)   #combine red mask and image
resultBlue = cv2.bitwise_and(resize, resize, mask=maskBlue)     #combined blue mask and image
resultGreen = cv2.bitwise_and(resize, resize, mask=maskGreen)   #combined green mask and image
#display images
cv2.imshow('maskGreen',maskGreen)
cv2.imshow('imGreen', resultGreen)
cv2.imshow('maskRed',maskRed)
cv2.imshow('im3Red',resultRed)
cv2.imshow('maskBlue',maskBlue)
cv2.imshow('im3Blue',resultBlue)
cv2.imshow('img',resize)
color2 = maskRed[230,1]
print(color2)
maskRedGray = cv2.cvtColor(resultRed, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',maskRedGray)
color3 = maskRedGray[10,10]
print(color3)
ret,thresh = cv2.threshold(maskRedGray, 27,55 ,0)
_,contours,hier = cv2.findContours(maskRed, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cnt1 = contours[0]
cnt2 = contours[1]
cv2.drawContours(resize, contours, -1, (20,220,20),3)
cv2.imshow('maskContours', resize)
cv2.waitKey(0)
