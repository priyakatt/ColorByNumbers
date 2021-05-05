<<<<<<< HEAD

=======
>>>>>>> 6983ab4ebfdf95c44cf9276d2ed5cacae544ddbc
import pygame
from pygame.locals import* #for event MOUSE variables
import os
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np

GPIO.setmode(GPIO.BCM) # set mode for broadcom numbering
#GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)


start_time = time.time()    #start time
timeOut = 30    #timeout after 30 seconds

#def GPIO27_callback(channel): #GPIO27 quit 
 #   print("Quit \n")
  #  global code_run
   # code_run=False  #set flag to 0 to tell main code to end

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
#my_font=pygame.font.Font(None,30)
#my_buttons = {'quit':(160, 180), 'touch at '+str(Xcoord) +', '+str(Ycoord):(160,100)}   #display dictionary
screen.fill(BLACK) #Erase workspace

#display initial screen
#for my_text, text_pos in my_buttons.items():    #cycle through dictionary to load text
   # text_surface = my_font.render(my_text, True, WHITE) #set button surface
   # rect = text_surface.get_rect(center=text_pos)
   # screen.blit(text_surface, rect) #combine surfaces
#pygame.display.flip()   #display working screen surface

#GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)   #GPIO27 quits script

xydata=[]   #initialize list to store x,y coordinate data
#dataFile=open("data_screen_coordinates.txt","w")    #open a txt file to write the data to


#Image Processing
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
light_G2 = np.array([60,102,153])
dark_G2 = np.array([61,255,255])
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
#cv2.imshow('red_list',mask_list[0])
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
result_all = [result_Red,result_Orange,result_Yellow,result_G1,result_G2,result_G3,result_B1,result_B2,result_B3,result_Purple,result_PurpPink,result_PinkRed,result_Grey];
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

contours_all = [contours_Red, contours_Orange, contours_Yellow, contours_G1, contours_G2, contours_G3, contours_B1, contours_B2, contours_B3, contours_Purple, contours_PurpPink, contours_PinkRed, contours_Grey]
c=0
while c <13:
    cv2.drawContours(canvas, contours_all[c], -1, (0,0,0),3)
    c = c+1

cv2.imwrite('canvas.png',canvas)
canvasPygame = pygame.image.load("canvas.png")
canvas_rect = canvasPygame.get_rect()
screen.blit(canvasPygame, canvas_rect)
pygame.display.flip()
#cv2.imshow('FINAL',canvas)

#END IMAGE PROCESSING






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
            print(str(x)+","+str(y))
            if canvas_screen ==True:
                #fillColor = (0,128,255)     #BGR
                # iterate through the 13 color sets to find which the pixel belongs to and fill that mask with fillColor
                j=0
                print('x')
                print(Xcoord)
                print('y')
                print(y)
                while j <13:
                    mask_check=mask_all[j]
                    print(mask_check[Ycoord,Xcoord])
                    #print('x')
                    #print(Xcoord)
                    #print('y')
                    #print(y)
                
                    if mask_check[Ycoord,Xcoord] ==255:
                        result_check = result_all[j]
                        fillColor = result_check[Ycoord,Xcoord]
                        print(fillColor)
                        fillB = int(fillColor[0])
                        fillG = int(fillColor[1])
                        fillR = int(fillColor[2])
                        cv2.fillPoly(canvas, contours_all[j],(fillB,fillG,fillR))
                        #print(x)
                        color_range = j
                        # display color pick screen
                        cv2.imwrite('canvas.png',canvas)
                        canvasPygame = pygame.image.load("canvas.png")
                        canvas_rect = canvasPygame.get_rect()
                        screen.fill(BLACK)
                        screen.blit(canvasPygame ,canvas_rect)
                        pygame.display.flip()
                        break
                    else:
                        j=j+1
                canvas_screen = not canvas_screen
            else:
                #find color of pick (x,y)
                # color_range corresponds to which color range the shape choice was from
                #fillColor = 
                fillB = int(fillColor[0])
                fillG = int(fillColor[1])
                fillR = int(fillColor[2])
                cv2.fillPoly(canvas,contours_all[color_range], (fillB,fillG,fillR))
                cv2.imwrite('canvas.png',canvas)
                canvasPygame = pygame.image.load("canvas.png")
                canvas_rect = canvasPygame.get_rect()
                screen.fill(BLACK)
                screen.blit(canvasPygame ,canvas_rect)
                pygame.display.flip()


            #cv2.imshow('Fill',canvas)
            #cv2.waitKey(0)

            #if y>160:   #quit button in range y>160 and 106<x<212
             #   if  x>106 and x<212:
              #      print("Screen Pressed")
               #     code_run=False
            #screen.fill(BLACK)  #erase workspace
           # my_buttons = {'quit':(160, 180), 'touch at '+str(Xcoord) +', '+str(Ycoord):(160,100)}
           # for my_text, text_pos in my_buttons.items():    #display buttons with new touch coordinates
            #    text_surface = my_font.render(my_text, True, WHITE)
             #   rect = text_surface.get_rect(center=text_pos)
              #  screen.blit(text_surface, rect)
               # pygame.display.flip()

#dataFile.write(str(xydata)+"\n")    #write saved data to text file
#dataFile.close()    #close text file
#print(str(xydata))  #print data
#GPIO.cleanup()  #cleanup
<<<<<<< HEAD

=======
>>>>>>> 6983ab4ebfdf95c44cf9276d2ed5cacae544ddbc
