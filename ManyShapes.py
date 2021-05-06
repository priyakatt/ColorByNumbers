import pygame
from pygame.locals import* #for event MOUSE variables
import os
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np

start_time = time.time()    #start time
timeOut = 1200    #timeout after 120 seconds
GPIO.setmode(GPIO.BCM) # set mode for broadcom numbering
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def GPIO27_callback(channel): #GPIO27 quit
    print("Quit \n")
    global code_run
    code_run=False  #set flag to 0 to tell main code to end

GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)   #GPIO27 quits script

#PiTFT
#os.putenv('SDL_VIDEODRIVER','fbcon') #Display on PiTFT
#os.putenv('SDL_FBDEV','/dev/fb1')
#os.putenv('SDL_MOUSEDRV','TSLIB') #Track mouse clicks on PiTFT
#os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

pygame.init()   #initialize pygame library
pygame.mouse.set_visible(True) #turn cursor on (VNC)
#pygame.mouse.set_visible(False) #turn cursor off (piTFT)
WHITE = 255,255,255
BLACK = 0,0,0
screen = pygame.display.set_mode((320,240))

Xcoord=0    #initialize x,y
Ycoord=0    
screen.fill(BLACK) #Erase workspace
#Image Processing
#monitor
canvas =cv2.imread('aXnc7xn.png',1)#load blank canvas
shape_canvas = cv2.imread('aXnc7xn.png',1)
#resize = cv2.imread('fruits.jpg',1)
resize = cv2.imread('6ukjvZN.png',1)
#h,w,c = resize.shape
#canvas = cv2.resize(canvas,(w/3,h/3))
#screen = pygame.display.set_mode((w/3,h/3))
#resize = cv2.resize(resize,(w/3,h/3))

#piTFT
#image = cv2.imread('fruits.jpg',1)
#image = cv2.imread('njcutuP.png',1)     #load image
#resize = cv2.resize(image, (320,240))
#anvas = cv2.resize(canvas, (320,240))
hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)   #Conveert from BGR to HSV

#Red
light_red = np.array([0,102,153])
dark_red = np.array([9,255,255])
#orange
light_orange = np.array([10,102,153])
dark_orange = np.array([20,255,255])
#Y
light_Y=np.array([21, 102.0, 153.0])
dark_Y=np.array([30.0, 255.0, 255.0])
#G1
light_G1 = np.array([31,102,153])
dark_G1 = np.array([47,255,255])
#G2
light_G2 = np.array([48,102,153])
dark_G2 = np.array([64,255,255])
#G3
light_G3 = np.array([65,102,153])
dark_G3 = np.array([80,255,255])
#B1
light_B1 = np.array([81,102,153])
dark_B1 = np.array([94,255,255])
#B2
light_B2 =np.array([95,102,153])
dark_B2 = np.array([108,255,255])
#B3
light_B3 = np.array([109,102,153])
dark_B3 =np.array([122,255,255])
#Purple
light_Purple = np.array([123,102,153])
dark_Purple = np.array([140,255,255])
#Purp/Pink
light_PurpPink = np.array([141,102,153])
dark_PurpPink = np.array([150,255,255])
#Pink/Red
light_PinkRed = np.array([151,102,153])
dark_PinkRed = np.array([179,255,255])
#Grey
light_Grey = np.array([0,0.0,64])
dark_Grey = np.array([0,0.0,255])
#Dark
light_dark = np.array([0,45,20])
dark_dark = np.array([179,101,153])
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
mask_dark = cv2.inRange(hsv_img,light_dark,dark_dark) #dark mask
mask_all = [mask_Red, mask_Orange,mask_Yellow,mask_G1,mask_G2,mask_G3,mask_B1,mask_B2,mask_B3,mask_Purple,mask_PurpPink,mask_PinkRed, mask_Grey,mask_dark]
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
result_dark = cv2.bitwise_and(resize,resize,mask=mask_dark)
result_all = [result_Red,result_Orange,result_Yellow,result_G1,result_G2,result_G3,result_B1,result_B2,result_B3,result_Purple,result_PurpPink,result_PinkRed,result_Grey,result_dark];
#Grey Scale
mask_Red_GS = cv2.cvtColor(result_Red, cv2.COLOR_BGR2GRAY)
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
_,contours_dark,hier = cv2.findContours(mask_dark, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#contours_B3=contours_B3[-2]

contours_all = [contours_Red, contours_Orange, contours_Yellow, contours_G1, contours_G2, contours_G3, contours_B1, contours_B2, contours_B3, contours_Purple, contours_PurpPink, contours_PinkRed, contours_Grey,contours_dark]
c=0
while c <13:
    cv2.drawContours(canvas, contours_all[c], -1, (0,0,0),1)
    c = c+1

cv2.imwrite('canvas.png',canvas)
canvasPygame = pygame.image.load("canvas.png")
canvas_rect = canvasPygame.get_rect()
screen.blit(canvasPygame, canvas_rect)
pygame.display.flip()
#cv2.imshow('FINAL',canvas)
#cv2.imshow('b1',mask_B1)
#cv2.imshow('b2',mask_B2)
#cv2.imshow('b3',mask_B3)
#cv2.imshow('purple',mask_Purple)
#cv2.imshow('PurpPink',mask_PurpPink)
#cv2.imshow('pinkred',mask_PinkRed)
#cv2.imshow('dark',mask_dark)
#cv2.waitKey(0)
#pause(20)
#END IMAGE PROCESSING

#Differentiate Shapes
shape = 0
red_shapes_tot = len(contours_Red)
red_shapes_list = []
#print(red_shapes_tot)
while shape < red_shapes_tot:
    #print(shape)
    cv2.drawContours(shape_canvas, contours_Red[shape], -1, (0,0,0),1)
    cv2.fillPoly(shape_canvas,contours_Red[shape], (0,0,0))
    mask_red_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
    red_shapes_list.append(mask_red_shape)
    shape_canvas[:]=(255,255,255)
    shape = shape +1

shape = 0
yellow_shapes_tot = len(contours_Yellow)
yellow_shapes_list = []
#print(yellow_shapes_tot)
while shape < yellow_shapes_tot:
    #print(shape)
    cv2.drawContours(shape_canvas, contours_Yellow[shape], -1, (0,0,0),1)
    cv2.fillPoly(shape_canvas,contours_Yellow[shape], (0,0,0))
    mask_yellow_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
    yellow_shapes_list.append(mask_yellow_shape)
    shape_canvas[:]=(255,255,255)
    shape = shape +1

shape = 0
B3_shapes_tot = len(contours_B3)
B3_shapes_list = []
print(B3_shapes_tot)
contours_a = contours_B3[0]
contours_b = contours_B3[1]
while shape < 1:
    print(shape)
    cv2.drawContours(shape_canvas, [contours_b], -1, (0,0,255),thickness=-1)
    #cv2.fillPoly(shape_canvas,pts=contours_B3, color=(0,0,255))
    cv2.imshow('filledshape',shape_canvas)
    mask_B3_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
    B3_shapes_list.append(mask_B3_shape)
    shape_canvas[:]=(255,255,255)
    shape = shape +1

print('done')
cv2.imshow('canvas',shape_canvas)
    #cv2.waitKey(0)
    #shape_canvas[:] = (255,255,255)
cv2.imshow('mask',B3_shapes_list[0])
#cv2.imshow('mask1',B3_shapes_list[1])
#cv2.imshow('mask2',B3_shapes_list[40])
print('I showed images')
cv2.waitKey(0)
    



canvas_screen = True
code_run=True   
while code_run:
    current_time = time.time()
    elapsed_time = current_time - start_time     #calculate time elapsed
    if elapsed_time > timeOut:   #quit if 30 seconds have elapsed
        print("time out")
        code_run=False
    for event in pygame.event.get():    #watch for mousebutton press
        if event.type is MOUSEBUTTONUP:   #touch input
            pos=pygame.mouse.get_pos()
            x,y=pos     #save x,y coordinates of touch
            Xcoord=x
            Ycoord=y
            #print(str(x)+","+str(y))
            if canvas_screen ==True:
                color_range=0
                while color_range <13:
                    mask_check=mask_all[color_range]
                    if mask_check[Ycoord,Xcoord] ==255:
                        if color_range ==0:
                            #orange_og = cv2.imread('oranges.png',1)
                            reds = cv2.imread('red_range.png',1)
                            reds_pygame = pygame.image.load("red_range.png")
                            reds_rect = reds_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(reds_pygame,reds_rect)
                            pygame.display.flip()

                        elif color_range ==1:
                            oranges_og = cv2.imread('orange_range.png',1)
                            oranges = cv2.resize(oranges_og, (320,240))
                            oranges_pygame = pygame.image.load("orange_range.png")
                            oranges_rect = oranges_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(oranges_pygame,oranges_rect)
                            pygame.display.flip()
                        elif color_range ==2:
                            yellows= cv2.imread('yellow_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            yellows_pygame = pygame.image.load("yellow_range.png")
                            yellows_rect = yellows_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(yellows_pygame,yellows_rect)
                            pygame.display.flip()
                        elif color_range ==3:
                            g1= cv2.imread('g1_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            g1_pygame = pygame.image.load("g1_range.png")
                            g1_rect = g1_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(g1_pygame,g1_rect)
                            pygame.display.flip()
                        elif color_range ==4:
                            g2= cv2.imread('g2_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            g2_pygame = pygame.image.load("g2_range.png")
                            g2_rect = g2_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(g2_pygame,g2_rect)
                            pygame.display.flip()

                        elif color_range ==5:
                            g3 = cv2.imread('g3_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            g3_pygame = pygame.image.load("g3_range.png")
                            g3_rect = g3_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(g3_pygame,g3_rect)
                            pygame.display.flip()
                        elif color_range ==6:
                            b1 = cv2.imread('b1_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            b1_pygame = pygame.image.load("b1_range.png")
                            b1_rect = b1_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(b1_pygame,b1_rect)
                            pygame.display.flip()
                        elif color_range ==7:
                            b2= cv2.imread('b2_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            b2_pygame = pygame.image.load("b2_range.png")
                            b2_rect = b2_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(b2_pygame,b2_rect)
                            pygame.display.flip()
                        elif color_range ==8:
                            b3 = cv2.imread('b3_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            b3_pygame = pygame.image.load("b3_range.png")
                            b3_rect = b3_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(b3_pygame,b3_rect)
                            pygame.display.flip()
                        elif color_range ==9:
                            purple= cv2.imread('purple_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            purple_pygame = pygame.image.load("purple_range.png")
                            purple_rect = purple_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(purple_pygame,purple_rect)
                            pygame.display.flip()
                        elif color_range ==10:
                            purplepink = cv2.imread('purplepink_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            purplepink_pygame = pygame.image.load("purplepink_range.png")
                            purplepink_rect = purplepink_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(purplepink_pygame,purplepink_rect)
                            pygame.display.flip()
                        elif color_range ==11:
                            pinkred = cv2.imread('pinkred_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            pinkred_pygame = pygame.image.load("pinkred_range.png")
                            pinkred_rect = pinkred_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(pinkred_pygame,pinkred_rect)
                            pygame.display.flip()
                        else:
                            grey= cv2.imread('grey_range.png',1)
                            #oranges = cv2.resize(oranges_og, (320,240))
                            grey_pygame = pygame.image.load("grey_range.png")
                            grey_rect = grey_pygame.get_rect()
                            screen.fill(BLACK)
                            screen.blit(grey_pygame,grey_rect)
                            pygame.display.flip()
                        break
                    else:
                        color_range=color_range+1
                canvas_screen = not canvas_screen
            else:
                #find color of pick (x,y)
                if color_range ==0:
                    fillColor = reds[Ycoord,Xcoord]
                elif color_range ==1:
                    fillColor = oranges[Ycoord,Xcoord]
                elif color_range ==2:
                    fillColor = yellows[Ycoord,Xcoord]
                elif color_range ==3:
                    fillColor = g1[Ycoord,Xcoord]
                elif color_range ==4:
                    fillColor = g2[Ycoord,Xcoord]
                elif color_range ==5:
                    fillColor = g3[Ycoord,Xcoord]
                elif color_range ==6:
                    fillColor = b1[Ycoord,Xcoord]
                elif color_range ==7:
                    fillColor = b2[Ycoord,Xcoord]
                elif color_range ==8:
                    fillColor = b3[Ycoord,Xcoord]
                elif color_range ==9:
                    fillColor = purple[Ycoord,Xcoord]
                elif color_range ==10:
                    fillColor = purplepink[Ycoord,Xcoord]
                elif color_range ==11:
                    fillColor = pinkred[Ycoord,Xcoord]
                elif color_range ==12:
                    fillColor = grey[Ycoord,Xcoord]
                else:
                    fillColor = resize[Ycoord,Xcoord]
                # color_range corresponds to which color range the shape choice was from
                fillB = int(fillColor[0])
                fillG = int(fillColor[1])
                fillR = int(fillColor[2])
                if color_range <13:
                    cv2.fillPoly(canvas,contours_all[color_range], (fillB,fillG,fillR))
                    cv2.imwrite('canvas.png',canvas)
                    canvasPygame = pygame.image.load("canvas.png")
                    canvas_rect = canvasPygame.get_rect()
                    screen.fill(BLACK)
                    screen.blit(canvasPygame ,canvas_rect)
                    pygame.display.flip()
                canvas_screen = not canvas_screen

            #cv2.imshow('Fill',canvas)
            #cv2.waitKey(0)
GPIO.cleanup()
