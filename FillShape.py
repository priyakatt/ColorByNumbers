# FillShape.py,
#Given a pixel, find mask/colorset and fill shape(s) with color
#
import cv2
import numpy as np

image = cv2.imread('njcutuP.png',1)     #load image
canvas = cv2.imread('aXnc7xn.png',1) # load blank canvas
resize = cv2.resize(image, (320,240))   #resize to PiTFT screen size
hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)   #Conveert from BGR to HSV

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
dark_B2 = np.array([106,255,255])
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
mask_all = [mask_Red, mask_Orange,mask_Yellow,mask_G1,mask_G2,mask_G3,mask_B1,mask_B2,mask_B3,mask_Purple,mask_PurpPink,mask_PinkRed, mask_Grey]
mask_list =[]
mask_list.append(mask_Red);
cv2.imshow('red_list',mask_list[0])
#Apply Masks
result_Red = cv2.bitwise_and(resize, resize, mask=mask_Red)   #combine red mask and image
result_Orange = cv2.bitwise_and(resize, resize, mask=mask_Orange)     #combined Orange mask and image
result_Yellow= cv2.bitwise_and(resize, resize, mask=mask_Yellow)   #combined yellow mask and image
result_G1 = cv2.bitwise_and(resize, resize, mask=mask_G1)   #combine G1 mask and image
result_G2 = cv2.bitwise_and(resize, resize, mask=mask_G2)     #combined G2 mask and image
result_G3= cv2.bitwise_and(resize, resize, mask=mask_G3)   #combined G3 mask and image
result_B1= cv2.bitwise_and(resize, resize, mask=mask_B1)   #combine B1 mask and image
result_B2 = cv2.bitwise_and(resize, resize, mask=mask_B2)     #combined B2 mask and image
result_B3= cv2.bitwise_and(resize, resize, mask=mask_B3)   #combined B3 mask and image
result_Purple = cv2.bitwise_and(resize, resize, mask=mask_Purple)   #combine Purple mask and image
result_PurpPink = cv2.bitwise_and(resize, resize, mask=mask_PurpPink)     #combined purple/pink mask and image
result_PinkRed= cv2.bitwise_and(resize, resize, mask=mask_PinkRed)   #combined pink/red  mask and image
result_Grey= cv2.bitwise_and(resize, resize, mask=mask_Grey)   #combined grey mask and image
# test coloring in a pixel -> use (y,x)
#result_Orange[160,10]=(0,0,255)
#cv2.imshow('res_or', result_Orange)
#resize[160,10]=(0,0,255)
#resize[161,10]=(0,0,255)
#cv2.imshow('res_pix',resize)

#display images
cv2.imshow('mask_G1',mask_G1)
cv2.imshow('mask_G2',mask_G2)
cv2.imshow('mask_G3',mask_G3)
cv2.imshow('mask_Purple', mask_Purple)
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

contours_all = [contours_Red, contours_Orange, contours_Yellow, contours_G1, contours_G3, contours_G3, contours_B1, contours_B2, contours_B3, contours_Purple, contours_PurpPink, contours_PinkRed, contours_Grey]
c=0
while c <13:
    cv2.drawContours(canvas, contours_all[c], -1, (0,0,0),3)
    c = c+1
cv2.imshow('FINAL',canvas)

# TEST (X,Y) vs (Y,X)
#print('orange')
#print(mask_Orange[pixelX,pixelY])   #result = 0 black
#print(mask_Orange[pixelY,pixelX])   #result = 255 white
#print('resize')
#print(resize[pixelX,pixelY])        # result = [204, 102, 0] BGR blue
#print(resize[pixelY,pixelX])    # Result = [0, 128, 255] BGR orange
#print('result orange')
#print(result_Orange[pixelX,pixelY])     #result = [0,0,0] BGR black
#print(result_Orange[pixelY,pixelX])     #result = [0,128,255] BGR orange

#hard code pixel
pixelX = 160
pixelY = 10
fillColor = (0,128,255)     #BGR
# iterate through the 13 color sets to find which the pixel belongs to and fill that mask with fillColor
x=0
while x <13:
    mask_check=mask_all[x]
    #print(mask_check[pixelY,pixelX])
    if mask_check[pixelY,pixelX] ==255:
        cv2.fillPoly(canvas, contours_all[x],fillColor)
        #print(x)
        break
    else:
        x=x+1

cv2.imshow('Fill',canvas)
cv2.waitKey(0)
