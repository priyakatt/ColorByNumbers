import cv2
import numpy as np
#import matplotlib.pyplot as plt

image = cv2.imread('3Ust9Lq.png',1)

resize = cv2.resize(image, (320,240))
#resize = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB)
#ret,thresh=cv2.threshold(resize,127,255,0)
#contours,hierarchy = cv2.findContours(thresh, 1, 2)
#cnt = contours[0]
#epsilon = 0.1*cv2.arcLength(cnt,True)
#approx = cv2.approxPolyDP(cnt,epsilon,True)
hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
color = image[10,10]
print(color)
#light_red = np.array([161,155,84])
light_red = np.array([0,200,200])
#dark_red=np.array([179,255,255])
dark_red = np.array([0,255,255])
light_blue =np.array ([94, 80, 2])
dark_blue =np.array([126,255,255])
light_green=np.array([25,52,72])
dark_green = np.array([102,255,255])
maskRed = cv2.inRange(hsv_img, light_red, dark_red)
maskBlue = cv2.inRange(hsv_img, light_blue, dark_blue)
maskGreen = cv2.inRange(hsv_img, light_green, dark_green)
resultRed = cv2.bitwise_and(resize, resize, mask=maskRed)
resultBlue = cv2.bitwise_and(resize, resize, mask=maskBlue)
resultGreen = cv2.bitwise_and(resize, resize, mask=maskGreen)
cv2.imshow('maskGreen',maskGreen)
cv2.imshow('imGreen', resultGreen)
cv2.imshow('maskRed',maskRed)
cv2.imshow('im3Red',resultRed)
cv2.imshow('maskBlue',maskBlue)
cv2.imshow('im3Blue',resultBlue)
#cv2.imshow('img1',image)
cv2.imshow('img',resize)
color2 = maskRed[230,1]
print(color2)
maskRedGray = cv2.cvtColor(resultRed, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',maskRedGray)
color3 = maskRedGray[10,10]
print(color3)
ret,thresh = cv2.threshold(maskRedGray, 27,55 ,0)
#contours, hierarchy,_ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
_,contours,hier = cv2.findContours(maskRed, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#cnt=contours[4]
#epsilon = 0.1*cv2.arcLength(cnt,True)
#approx = cv2.approxPolyDP(cnt,epsilon,True)
#cv2.drawContours(maskRedGray,contours, -1, (0,255,0),3)
cnt1 = contours[0]
cnt2 = contours[1]
cv2.drawContours(resize, contours, -1, (20,220,20),3)
cv2.imshow('maskContours', resize)
cv2.waitKey(0)
