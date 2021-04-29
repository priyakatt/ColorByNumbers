#
# ImgProcExp.py, Expanded imaging processing
#Load an image,segment image into color ranges using masks, find shapes from masks
#
import cv2
import numpy as np

image = cv2.imread('njcutuP.png',1)     #load image
canvas = cv2.imread('aXnc7xn.png',1) # load blank canvas
resize = cv2.resize(image, (320,240))   #resize to PiTFT screen size
hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)   #Conveert from BGR to HSV
color = image[10,10]    #test what color pixel 10,10 is
print(color)
#light_red = np.array([0,200,200])   #Light red range
#dark_red = np.array([0,255,255])    #Dark Red Range
#light_B1 =np.array ([94, 80, 2])  #Light Blue Range
#dark_B1 =np.array([126,255,255])  #Dark Blue Range
#light_green=np.array([25,52,72])    #light Green Range
#dark_green = np.array([102,255,255])    #Dark Green Range

#Red
light_red = np.array([0.0,102,153])
dark_red = np.array([0.0,255,255])
#orange
light_orange = np.array([14,102,153])
dark_orange = np.array([15,255,255])
#Y
light_Y=np.array([30.0, 102.0, 153.0])
dark_Y=np.array([30.0, 255.0, 255.0])
#G1
light_G1 = np.array([45,102,153])
dark_G1 = np.array([46,255,255])
#G2
light_G2 = np.array([60,102,153.0])
dark_G2 = np.array([60.0,255,255])
#G3
light_G3 = np.array([74,102,153])
dark_G3 = np.array([75,255,255])
#B1
light_B1 = np.array([90,102,153])
dark_B1 = np.array([90,255,255])
#B2
light_B2 =np.array([105,102,153])
dark_B2 = np.array([151,255,255])
#B3
light_B3 = np.array([120,102,153])
dark_B3 =np.array([120,255,255])
#Purple
light_Purple = np.array([134,102,153])
dark_Purple = np.array([135,255,255])
#Purp/Pink
light_PurpPink = np.array([150,102,153])
dark_PurpPink = np.array([150,255,255])
#Pink/Red
light_PinkRed = np.array([165,102,153])
dark_PinkRed = np.array([166,255,255])
#Grey
light_Grey = np.array([0,0.0,64])
dark_Grey = np.array([0,0.0,224])

#Color Masks
mask_Red = cv2.inRange(hsv_img, light_red, dark_red)     #red mask
mask_Orange = cv2.inRange(hsv_img, light_orange, dark_orange)  #orange mask
mask_Yellow = cv2.inRange(hsv_img, light_Y, dark_Y)   #Yellow mask
mask_G1 = cv2.inRange(hsv_img, light_G1, dark_G1)     #red mask
mask_G2 = cv2.inRange(hsv_img, light_G2, dark_G2)  #orange mask
mask_G3 = cv2.inRange(hsv_img, light_G3, dark_G3)   #Yellow mask
mask_B1 = cv2.inRange(hsv_img, light_B1, dark_B1)     #red mask
mask_B2 = cv2.inRange(hsv_img, light_B2, dark_B2)  #orange mask
mask_B3 = cv2.inRange(hsv_img, light_B3, dark_B3)   #Yellow mask
mask_Purple = cv2.inRange(hsv_img, light_Purple, dark_Purple)     #red mask
mask_PurpPink = cv2.inRange(hsv_img, light_PurpPink, dark_PurpPink)  #orange mask
mask_PinkRed = cv2.inRange(hsv_img, light_PinkRed, dark_PinkRed)   #Yellow mask
mask_Grey = cv2.inRange(hsv_img, light_Grey, dark_Grey)     #red mask

#Apply Masks
result_Red = cv2.bitwise_and(resize, resize, mask=mask_Red)   #combine red mask and image
result_Orange = cv2.bitwise_and(resize, resize, mask=mask_Orange)     #combined Orange mask and image
result_Yellow= cv2.bitwise_and(resize, resize, mask=mask_Yellow)   #combined yellow mask and image
result_G1 = cv2.bitwise_and(resize, resize, mask=mask_G1)   #combine red mask and image
result_G2 = cv2.bitwise_and(resize, resize, mask=mask_G2)     #combined Orange mask and image
result_G3= cv2.bitwise_and(resize, resize, mask=mask_G3)   #combined yellow mask and image
result_B1= cv2.bitwise_and(resize, resize, mask=mask_B1)   #combine red mask and image
result_B2 = cv2.bitwise_and(resize, resize, mask=mask_B2)     #combined Orange mask and image
result_B3= cv2.bitwise_and(resize, resize, mask=mask_B3)   #combined yellow mask and image
result_Purple = cv2.bitwise_and(resize, resize, mask=mask_Purple)   #combine red mask and image
result_PurpPink = cv2.bitwise_and(resize, resize, mask=mask_PurpPink)     #combined Orange mask and image
result_PinkRed= cv2.bitwise_and(resize, resize, mask=mask_PinkRed)   #combined yellow mask and image
result_Grey= cv2.bitwise_and(resize, resize, mask=mask_Grey)   #combined yellow mask and image
#display images
#cv2.imshow('maskGreen',maskGreen)
#cv2.imshow('imGreen', resultGreen)
#cv2.imshow('maskRed',maskRed)
#cv2.imshow('im3Red',resultRed)
#cv2.imshow('maskBlue',maskBlue)
#cv2.imshow('im3Blue',resultBlue)
#cv2.imshow('img',resize)
#color2 = maskRed[230,1]
#print(color2)

#Grey Scale
mask_Red_GS = cv2.cvtColor(result_Red, cv2.COLOR_BGR2GRAY)
mask_Orange_GS = cv2.cvtColor(result_Orange, cv2.COLOR_BGR2GRAY)
mask_Yellow_GS = cv2.cvtColor(result_Yellow, cv2.COLOR_BGR2GRAY)
mask_G1_GS = cv2.cvtColor(result_G1, cv2.COLOR_BGR2GRAY)
mask_G2_GS = cv2.cvtColor(result_G2, cv2.COLOR_BGR2GRAY)
mask_G3_GS = cv2.cvtColor(result_G3, cv2.COLOR_BGR2GRAY)
mask_B1_GS = cv2.cvtColor(result_B1, cv2.COLOR_BGR2GRAY)
mask_B2_GS = cv2.cvtColor(result_B2, cv2.COLOR_BGR2GRAY)
mask_B3_GS = cv2.cvtColor(result_B3, cv2.COLOR_BGR2GRAY)
mask_Purple_GS = cv2.cvtColor(result_Purple, cv2.COLOR_BGR2GRAY)
mask_PurpPink_GS = cv2.cvtColor(result_PurpPink, cv2.COLOR_BGR2GRAY)
mask_PinkRed_GS = cv2.cvtColor(result_PinkRed, cv2.COLOR_BGR2GRAY)
mask_Grey_GS = cv2.cvtColor(result_Grey, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',maskRedGray)
#print(color3)
ret,thresh = cv2.threshold(mask_Red_GS, 27,55 ,0)
#Color Contours
_,contours_Red,hier = cv2.findContours(mask_Red, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_Orange,hier = cv2.findContours(mask_Orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_Yellow,hier = cv2.findContours(mask_Yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_G1,hier = cv2.findContours(mask_G1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_G2,hier = cv2.findContours(mask_G2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_G3,hier = cv2.findContours(mask_G3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_B1,hier = cv2.findContours(mask_B1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_B2,hier = cv2.findContours(mask_B2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_B3,hier = cv2.findContours(mask_B3, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_Purple,hier = cv2.findContours(mask_Purple, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_PurpPink,hier = cv2.findContours(mask_PurpPink, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_PinkRed,hier = cv2.findContours(mask_PinkRed, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
_,contours_Grey,hier = cv2.findContours(mask_Grey, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(canvas, contours_Red, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_Orange, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_Yellow, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_G1, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_G2, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_G3, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_B1, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_B2, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_B3, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_Purple, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_PurpPink, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_PinkRed, -1, (0,0,0),3)
cv2.drawContours(canvas, contours_Grey, -1, (0,0,0),3)

cv2.imshow('mask_Red', mask_Red)
cv2.imshow('mask_O', mask_Orange)
cv2.imshow('mask_Y', mask_Yellow)
cv2.imshow('mask_G1', mask_G1)
cv2.imshow('mask_G2', mask_G2)
cv2.imshow('mask_G3', mask_G3)
cv2.imshow('mask_B1',mask_B1)
cv2.imshow('FINAL',canvas)
cv2.waitKey(0)
