# Pitft_Final.py Final Project PiTFT implementation
# mm2563, psk92

import pygame
from pygame.locals import* #for event MOUSE variables
import os
import RPi.GPIO as GPIO
import time
import cv2
import numpy as np

start_time = time.time()    #start time
timeOut = 300    #timeout after 300 seconds
#--------GPIO---------
GPIO.setmode(GPIO.BCM) # set mode for broadcom numbering
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def GPIO23_callback(channel): #GPIO23
    global draw_screen
    draw_screen = not draw_screen
    if draw_screen==False:
        screen.fill(BLACK)
        screen.blit(resize_pygame ,resize_rect)
        pygame.display.flip()
        
    else:
        #display canvas
        screen.fill(BLACK)
        screen.blit(canvasPygame ,canvas_rect)
        pygame.display.flip()
def GPIO27_callback(channel): #GPIO27 quit
    print("Quit \n")
    global code_run
    code_run=False  #set flag to 0 to tell main code to end

def GPIO22_callback(channel): #GPIO22
    global menu_screen, start_screen, pick_image_screen
    if start_screen==True or pick_image_screen==True:
        menu_screen=False
    else:
        menu_screen=True
        screen.fill(BLACK)
        for my_text, text_pos in menu_buttons.items():    #cycle through dictionary to load value
            text_surface = my_font.render(my_text, True, WHITE) #setup button surface
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface, rect) #combine surfaces
        pygame.display.flip()   #display working screen surface


GPIO.add_event_detect(27, GPIO.FALLING, callback=GPIO27_callback, bouncetime=300)   #GPIO27 quits script
GPIO.add_event_detect(23, GPIO.FALLING, callback=GPIO23_callback, bouncetime=300)   #GPIO23 changes screen
GPIO.add_event_detect(22, GPIO.FALLING, callback=GPIO22_callback, bouncetime=300)   #GPIO22 changes screen


#---------PiTFT/VNC-------
os.putenv('SDL_VIDEODRIVER','fbcon') #Display on PiTFT
os.putenv('SDL_FBDEV','/dev/fb1')
os.putenv('SDL_MOUSEDRV','TSLIB') #Track mouse clicks on PiTFT
os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

pygame.init()   #initialize pygame library
#pygame.mouse.set_visible(True) #turn cursor on (VNC)
pygame.mouse.set_visible(False) #turn cursor off (piTFT)
WHITE = 255,255,255
BLACK = 0,0,0
screen = pygame.display.set_mode((320,240))

Xcoord=0    #initialize x,y
Ycoord=0    
screen.fill(BLACK) #Erase workspace
#----------Button-------
pygame.init()
my_font=pygame.font.Font(None,30)
my_buttons = {'Color By Numbers':(160, 80), 'Free Color':(160,160)}    #buttons
menu_buttons = {'Change Mode':(160, 60), 'New Image':(160,120),'Save Image':(160,180)}    #Menu buttons

screen.fill(BLACK) #Erase workspace

for my_text, text_pos in my_buttons.items():    #cycle through dictionary to load value
    text_surface = my_font.render(my_text, True, WHITE) #setup button surface
    rect = text_surface.get_rect(center=text_pos)
    screen.blit(text_surface, rect) #combine surfaces

pygame.display.flip()   #display working screen surface
#-------Upload Images for selection------
image1_pygame = pygame.image.load("ocean.jpg")
image1_rect = image1_pygame.get_rect()
image2_pygame = pygame.image.load("Cornell.jpg")
image2_rect = image2_pygame.get_rect()
image3_pygame = pygame.image.load("puzzle.png")
image3_rect = image3_pygame.get_rect()
image4_pygame = pygame.image.load("pinkflowers.png")
image4_rect = image4_pygame.get_rect()

#Shrink
image1_shrink_py = pygame.transform.scale(image1_pygame,(160,120))
image1_rect = image1_rect.move(0,0)
image2_shrink_py = pygame.transform.scale(image2_pygame,(160,120))
image2_rect = image2_rect.move(0,120)
image3_shrink_py = pygame.transform.scale(image3_pygame,(160,120))
image3_rect = image3_rect.move(160,0)
image4_shrink_py = pygame.transform.scale(image4_pygame,(160,120))
image4_rect = image4_rect.move(160,120)
#--------Image Processing--------
#monitor
canvas =cv2.imread('aXnc7xn.png',1)#load blank canvas
shape_canvas = cv2.imread('aXnc7xn.png',1)
all_colors = cv2.imread('allcolors.png',1)
all_colors_pygame = pygame.image.load('allcolors.png')
all_colors_rect = all_colors_pygame.get_rect()
#----Load Color Range Images-------
reds = cv2.imread('red_range.png',1)
reds_pygame = pygame.image.load("red_range.png")
reds_rect = reds_pygame.get_rect()
oranges = cv2.imread('orange_range.png',1)
oranges_pygame = pygame.image.load("orange_range.png")
oranges_rect = oranges_pygame.get_rect()
yellows= cv2.imread('yellow_range.png',1)
yellows_pygame = pygame.image.load("yellow_range.png")
yellows_rect = yellows_pygame.get_rect()
g1= cv2.imread('g1_range.png',1)
g1_pygame = pygame.image.load("g1_range.png")
g1_rect = g1_pygame.get_rect()
g2= cv2.imread('g2_range.png',1)
g2_pygame = pygame.image.load("g2_range.png")
g2_rect = g2_pygame.get_rect()
g3 = cv2.imread('g3_range.png',1)
g3_pygame = pygame.image.load("g3_range.png")
g3_rect = g3_pygame.get_rect()
b1 = cv2.imread('b1_range.png',1)
b1_pygame = pygame.image.load("b1_range.png")
b1_rect = b1_pygame.get_rect()
b2= cv2.imread('b2_range.png',1)
b2_pygame = pygame.image.load("b2_range.png")
b2_rect = b2_pygame.get_rect()
b3 = cv2.imread('b3_range.png',1)
b3_pygame = pygame.image.load("b3_range.png")
b3_rect = b3_pygame.get_rect()
purple= cv2.imread('purple_range.png',1)
purple_pygame = pygame.image.load("purple_range.png")
purple_rect = purple_pygame.get_rect()
purplepink = cv2.imread('purplepink_range.png',1)
purplepink_pygame = pygame.image.load("purplepink_range.png")
purplepink_rect = purplepink_pygame.get_rect()
pinkred = cv2.imread('pinkred_range.png',1)
pinkred_pygame = pygame.image.load("pinkred_range.png")
pinkred_rect = pinkred_pygame.get_rect()
grey= cv2.imread('grey_range.png',1)
grey_pygame = pygame.image.load("grey_range.png")
grey_rect = grey_pygame.get_rect()
#--------Set Color Ranges-------
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
dark_Grey = np.array([0,0.0,229])
#Dark
light_dark = np.array([0,45,20])
dark_dark = np.array([179,101,153])

def imageProcessing(hsv_img,resize):
    global canvasPygame, canvas_rect
    global contours_Red, contours_Orange, contours_Yellow, contours_G1, contours_G2, contours_G3, contours_B1, contours_B2, contours_B3, contours_Purple, contours_PurpPink, contours_PinkRed, contours_Grey,contours_dark, contours_all
    global red_shapes_tot, red_shapes_list, orange_shapes_tot, orange_shapes_list, yellow_shapes_tot, yellow_shapes_list, G1_shapes_tot, G1_shapes_list, G2_shapes_tot, G2_shapes_list, G3_shapes_tot, G3_shapes_list, B1_shapes_tot, B1_shapes_list, B2_shapes_tot, B2_shapes_list, B3_shapes_tot , B3_shapes_list, Purple_shapes_tot, Purple_shapes_list, PurpPink_shapes_tot, PurpPink_shapes_list, PinkRed_shapes_tot , PinkRed_shapes_list, Grey_shapes_tot, Grey_shapes_list, dark_shapes_tot, dark_shapes_list
    global mask_all, mask_Red, mask_Orange, mask_Yellow, mask_G1, mask_G2, mask_G3, mask_B1, mask_B2, mask_B3, mask_Purple, mask_PurpPink, mask_PinkRed, mask_Grey, mask_dark
    #-----------Color Masks-----------
    mask_Red = cv2.inRange(hsv_img, light_red, dark_red)     #red mask
    mask_Orange = cv2.inRange(hsv_img, light_orange, dark_orange)  #orange mask
    mask_Yellow = cv2.inRange(hsv_img, light_Y, dark_Y)   #Yellow mask
    mask_G1 = cv2.inRange(hsv_img, light_G1, dark_G1)     #G1 mask
    mask_G2 = cv2.inRange(hsv_img, light_G2, dark_G2)  #G2 mask
    mask_G3 = cv2.inRange(hsv_img, light_G3, dark_G3)   #G3 mask
    mask_B1 = cv2.inRange(hsv_img, light_B1, dark_B1)     #B1 mask
    mask_B2 = cv2.inRange(hsv_img, light_B2, dark_B2)  #B2 mask
    mask_B3 = cv2.inRange(hsv_img, light_B3, dark_B3)   #B3 mask
    mask_Purple = cv2.inRange(hsv_img, light_Purple, dark_Purple)     #Purple mask
    mask_PurpPink = cv2.inRange(hsv_img, light_PurpPink, dark_PurpPink)  #Purple/Pink mask
    mask_PinkRed = cv2.inRange(hsv_img, light_PinkRed, dark_PinkRed)   #Pink/Red mask
    mask_Grey = cv2.inRange(hsv_img, light_Grey, dark_Grey)     #Grey mask
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
    result_dark = cv2.bitwise_and(resize,resize,mask=mask_dark)     #combined dark mask and image
    result_all = [result_Red,result_Orange,result_Yellow,result_G1,result_G2,result_G3,result_B1,result_B2,result_B3,result_Purple,result_PurpPink,result_PinkRed,result_Grey,result_dark];
    #Grey Scale
    mask_Red_GS = cv2.cvtColor(result_Red, cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(mask_Red_GS, 27,55 ,0)
    #-------------Color Contours-------------
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

    contours_all = [contours_Red, contours_Orange, contours_Yellow, contours_G1, contours_G2, contours_G3, contours_B1, contours_B2, contours_B3, contours_Purple, contours_PurpPink, contours_PinkRed, contours_Grey,contours_dark]
    c=0
    while c <13:
        cv2.drawContours(canvas, contours_all[c], -1, (0,0,0),1)
        c = c+1

    cv2.imwrite('canvas.png',canvas)
    canvasPygame = pygame.image.load("canvas.png")
    canvas_rect = canvasPygame.get_rect()
    #----------END IMAGE PROCESSING----------

    #----------Differentiate Shapes---------
    shape = 0
    red_shapes_tot = len(contours_Red)  #RED
    red_shapes_list = []
    while shape < red_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_Red[shape]], -1, (0,0,0),thickness=-1)
        mask_red_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        red_shapes_list.append(mask_red_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape=0
    orange_shapes_tot = len(contours_Orange)   #ORANGE
    orange_shapes_list = []
    while shape < orange_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_Orange[shape]], -1, (0,0,0),thickness=-1)
        mask_orange_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        orange_shapes_list.append(mask_orange_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape = 0
    yellow_shapes_tot = len(contours_Yellow)    #YELLOW
    yellow_shapes_list = []
    while shape < yellow_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_Yellow[shape]], -1, (0,0,0),thickness=-1)
        mask_yellow_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        yellow_shapes_list.append(mask_yellow_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape=0
    G1_shapes_tot = len(contours_G1)      #G1
    G1_shapes_list = []
    while shape < G1_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_G1[shape]], -1, (0,0,0),thickness=-1)
        mask_G1_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        G1_shapes_list.append(mask_G1_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape=0
    G2_shapes_tot = len(contours_G2)  #G2
    G2_shapes_list = []
    while shape < G2_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_G2[shape]], -1, (0,0,0),thickness=-1)
        mask_G2_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        G2_shapes_list.append(mask_G2_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape =0
    G3_shapes_tot = len(contours_G3)  #G3
    G3_shapes_list = []
    while shape < G3_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_G3[shape]], -1, (0,0,0),thickness=-1)
        mask_G3_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        G3_shapes_list.append(mask_G3_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape=0
    B1_shapes_tot = len(contours_B1)  #B1
    B1_shapes_list = []
    while shape < B1_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_B1[shape]], -1, (0,0,0),thickness=-1)
        mask_B1_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        B1_shapes_list.append(mask_B1_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape=0
    B2_shapes_tot = len(contours_B2)  #B2
    B2_shapes_list = []
    while shape < B2_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_B2[shape]], -1, (0,0,0),thickness=-1)
        mask_B2_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        B2_shapes_list.append(mask_B2_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1

    shape = 0
    B3_shapes_tot = len(contours_B3)    #B3
    B3_shapes_list = []
    #contours_b = contours_B3[1]
    while shape < B3_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_B3[shape]], -1, (0,0,0),thickness=-1)
        mask_B3_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        B3_shapes_list.append(mask_B3_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape=0
    Purple_shapes_tot = len(contours_Purple)  #Purple
    Purple_shapes_list = []
    while shape < Purple_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_Purple[shape]], -1, (0,0,0),thickness=-1)
        mask_Purple_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        Purple_shapes_list.append(mask_Purple_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1

    shape = 0
    PurpPink_shapes_tot = len(contours_PurpPink)  #PurpPink
    PurpPink_shapes_list = []
    while shape < PurpPink_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_PurpPink[shape]], -1, (0,0,0),thickness=-1)
        mask_PurpPink_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        PurpPink_shapes_list.append(mask_PurpPink_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1

    shape = 0
    PinkRed_shapes_tot = len(contours_PinkRed)  #PinkRed
    PinkRed_shapes_list = []
    while shape < PinkRed_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_PinkRed[shape]], -1, (0,0,0),thickness=-1)
        mask_PinkRed_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        PinkRed_shapes_list.append(mask_PinkRed_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1

    shape = 0
    Grey_shapes_tot = len(contours_Grey)    #Grey
    Grey_shapes_list = []
    while shape < Grey_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_Grey[shape]], -1, (0,0,0),thickness=-1)
        mask_Grey_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        Grey_shapes_list.append(mask_Grey_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1
    shape = 0
    dark_shapes_tot = len(contours_dark)      #dark
    dark_shapes_list = []
    while shape < dark_shapes_tot:
        cv2.drawContours(shape_canvas, [contours_dark[shape]], -1, (0,0,0),thickness=-1)
        mask_dark_shape = cv2.inRange(shape_canvas, (0,0,0),(180,255,255))
        dark_shapes_list.append(mask_dark_shape)
        shape_canvas[:]=(255,255,255)
        shape = shape +1

#-------END Differentiate Shapes-------

#-------MAIN-----------
draw_screen=True
canvas_screen = True
code_run=True 
free_play = True
normal_play=False
hue_screen=False
free_color_range=13
start_screen=True
pick_image_screen=False
menu_screen=False
new_mode=False
while code_run:
    current_time = time.time()
    elapsed_time = current_time - start_time     #calculate time elapsed
    if elapsed_time > timeOut:   #quit if 30 seconds have elapsed
        print("time out")
        code_run=False
    for event in pygame.event.get():    #watch for mousebutton press
        if event.type is MOUSEBUTTONUP:   #touch input
            draw_screen=True
            pos=pygame.mouse.get_pos()
            x,y=pos     #save x,y coordinates of touch
            Xcoord=x
            Ycoord=y
            if start_screen==True:
                if Ycoord<120:
                    normal_play=True
                    free_play=False
                else:
                    normal_play=False
                    free_play=True
                start_screen= not start_screen
                if new_mode ==False:
                    pick_image_screen=True
                    screen.fill(BLACK)
                    screen.blit(image1_shrink_py, image1_rect)
                    screen.blit(image2_shrink_py, image2_rect)
                    screen.blit(image3_shrink_py, image3_rect)
                    screen.blit(image4_shrink_py, image4_rect)
                    pygame.display.flip()
                else:
                    screen.fill(BLACK)
                    screen.blit(canvasPygame ,canvas_rect)
                    pygame.display.flip()
            elif menu_screen==True:     #New Mode
                if Ycoord<=80:
                    print('New Mode')
                    start_screen=True
                    screen.fill(BLACK) #Erase workspace
                    new_mode = True

                    for my_text, text_pos in my_buttons.items():    #cycle through dictionary to load value
                        text_surface = my_font.render(my_text, True, WHITE) #setup button surface
                        rect = text_surface.get_rect(center=text_pos)
                        screen.blit(text_surface, rect) #combine surfaces

                    pygame.display.flip()   #display working screen surface

                elif Ycoord>80 and Ycoord <160:     #New Image
                    pick_image_screen=True
                    print('New Image')
                    canvas =cv2.imread('aXnc7xn.png',1)#load blank canvas
                    canvasPygame = pygame.image.load("canvas.png")
                    canvas_rect = canvasPygame.get_rect()
                    screen.fill(BLACK)
                    screen.blit(image1_shrink_py, image1_rect)
                    screen.blit(image2_shrink_py, image2_rect)
                    screen.blit(image3_shrink_py, image3_rect)
                    screen.blit(image4_shrink_py, image4_rect)
                    pygame.display.flip()
                elif Ycoord>=160:    #save image
                    print('save image')
                    pygame.image.save(canvasPygame, 'user_image.png')

                menu_screen=False

            elif pick_image_screen==True:
                #display 4 images
                if Xcoord<160 and Ycoord<120: #image 1
                    resize = cv2.imread('ocean.jpg',1)
                    resize = cv2.resize(resize, (320,240))
                    resize_pygame = pygame.image.load('ocean.jpg')
                    resize_pygame =  pygame.transform.scale(resize_pygame,(320,240))
                    resize_rect = resize_pygame.get_rect()
                    hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
                    imageProcessing(hsv_img,resize)
                elif Xcoord>160 and Ycoord <120: #Image 3
                    resize = cv2.imread('puzzle.png',1)
                    resize = cv2.resize(resize, (320,240))
                    resize_pygame = pygame.image.load('puzzle.png')
                    resize_pygame =  pygame.transform.scale(resize_pygame,(320,240))
                    resize_rect = resize_pygame.get_rect()
                    hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
                    imageProcessing(hsv_img,resize)
                elif Xcoord <160 and Ycoord >120: #Image 2
                    resize = cv2.imread('Cornell.jpg',1)
                    resize = cv2.resize(resize, (320,240))
                    resize_pygame = pygame.image.load('Cornell.jpg')
                    resize_pygame =  pygame.transform.scale(resize_pygame,(320,240))
                    resize_rect = resize_pygame.get_rect()
                    hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
                    imageProcessing(hsv_img,resize)
                else: #Image 4
                    resize = cv2.imread('pinkflowers.png',1)
                    resize = cv2.resize(resize, (320,240))
                    resize_pygame = pygame.image.load('pinkflowers.png')
                    resize_pygame =  pygame.transform.scale(resize_pygame,(320,240))
                    resize_rect = resize_pygame.get_rect()
                    hsv_img = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
                    imageProcessing(hsv_img,resize)
                pick_image_screen=False
                screen.fill(BLACK)
                screen.blit(canvasPygame,canvas_rect)
                pygame.display.flip()

            elif canvas_screen ==True:
                found_shape=False
                color_range=0
                while color_range <13:
                    mask_check=mask_all[color_range]
                    if mask_check[Ycoord,Xcoord] ==255:
                        if color_range ==0:             #RED
                            #search shapes
                            shape_num =0
                            while shape_num<red_shapes_tot:
                                red_check = red_shapes_list[shape_num]
                                if red_check[Ycoord,Xcoord]==255: 
                                    if normal_play==True:     #Display red color gradient
                                        screen.fill(BLACK)
                                        screen.blit(reds_pygame,reds_rect)
                                        break
                                    else:
                                        #display hue selection image
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==1:           #ORANGE
                            #search shapes
                            shape_num =0
                            while shape_num<orange_shapes_tot:
                                orange_check = orange_shapes_list[shape_num]
                                if orange_check[Ycoord,Xcoord]==255:
                                    if normal_play ==True:
                                        screen.fill(BLACK)
                                        screen.blit(oranges_pygame,oranges_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                     shape_num = shape_num+1
                        elif color_range ==2:           #YELLOW
                            #search shapes
                            shape_num =0
                            while shape_num<yellow_shapes_tot:
                                yellow_check = yellow_shapes_list[shape_num]
                                if yellow_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(yellows_pygame,yellows_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==3:           #G1
                            #search shapes
                            shape_num =0
                            while shape_num<G1_shapes_tot:
                                G1_check = G1_shapes_list[shape_num]
                                if G1_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(g1_pygame,g1_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==4:           #G2
                            #search shapes
                            shape_num =0
                            while shape_num<G2_shapes_tot:
                                G2_check = G2_shapes_list[shape_num]
                                if G2_check[Ycoord,Xcoord]==255:
                                    if normal_play ==True:
                                        screen.fill(BLACK)
                                        screen.blit(g2_pygame,g2_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1

                        elif color_range ==5:           #G3
                            #search shapes
                            shape_num =0
                            while shape_num<G3_shapes_tot:
                                G3_check = G3_shapes_list[shape_num]
                                if G3_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(g3_pygame,g3_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==6:           #B1
                            #search shapes
                            shape_num =0
                            while shape_num<B1_shapes_tot:
                                B1_check = B1_shapes_list[shape_num]
                                if B1_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(b1_pygame,b1_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==7:           #B2
                            #search shapes
                            shape_num =0
                            while shape_num<B2_shapes_tot:
                                B2_check = B2_shapes_list[shape_num]
                                if B2_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(b2_pygame,b2_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==8:           #B3
                            #search shapes
                            shape_num =0
                            while shape_num<B3_shapes_tot:
                                B3_check = B3_shapes_list[shape_num]
                                if B3_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(b3_pygame,b3_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==9:           #PURPLE
                            #search shapes
                            shape_num =0
                            while shape_num<Purple_shapes_tot:
                                Purple_check = Purple_shapes_list[shape_num]
                                if Purple_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(purple_pygame,purple_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==10:          #PURPLE/PINK
                            #search shapes
                            shape_num =0
                            while shape_num<PurpPink_shapes_tot:
                                PurpPink_check = PurpPink_shapes_list[shape_num]
                                if PurpPink_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(purplepink_pygame,purplepink_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        elif color_range ==11:          #PINK/RED
                            #search shapes
                            shape_num =0
                            while shape_num<PinkRed_shapes_tot:
                                PinkRed_check = PinkRed_shapes_list[shape_num]
                                if PinkRed_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(pinkred_pygame,pinkred_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        else:           #GREY
                            #search shapes
                            shape_num =0
                            while shape_num<Grey_shapes_tot:
                                Grey_check = Grey_shapes_list[shape_num]
                                if Grey_check[Ycoord,Xcoord]==255:
                                    if normal_play==True:
                                        screen.fill(BLACK)
                                        screen.blit(grey_pygame,grey_rect)
                                        break
                                    else:
                                        found_shape=True
                                        break
                                else:
                                    shape_num = shape_num+1
                        break
                    else:
                        color_range=color_range+1
                if found_shape==True and free_play ==True:
                    #display hue screen
                    screen.fill(BLACK)
                    screen.blit(all_colors_pygame ,all_colors_rect)
                    hue_screen=True
                canvas_screen = not canvas_screen
                pygame.display.flip()
            elif hue_screen==True:
                #match x,y to hue
                hue = all_colors[Ycoord,Xcoord]
                hue_int =np.uint8([[[int(hue[0]),int(hue[1]),int(hue[2])]]])
                hsv_hue = cv2.cvtColor(hue_int,cv2.COLOR_BGR2HSV)
                screen.fill(BLACK)
                if hsv_hue[0][0][1]==0:   #grey
                    screen.blit(grey_pygame,grey_rect)
                    free_color_range=12
                elif hsv_hue[0][0][0] >=0 and hsv_hue[0][0][0] <=9:   #RED
                    screen.blit(reds_pygame,reds_rect)
                    free_color_range=0
                elif hsv_hue[0][0][0] >9 and hsv_hue[0][0][0]<=20:     #Orange
                    screen.blit(oranges_pygame,oranges_rect)
                    free_color_range=1
                elif hsv_hue[0][0][0] >20 and hsv_hue[0][0][0]<=30:     #Yellow
                    screen.blit(yellows_pygame,yellows_rect)
                    free_color_range=2
                elif hsv_hue[0][0][0] >30 and hsv_hue[0][0][0]<=47:     #G1
                    screen.blit(g1_pygame,g1_rect)
                    free_color_range=3
                elif hsv_hue[0][0][0] >47 and hsv_hue[0][0][0]<=64:   #G2
                    screen.blit(g2_pygame,g2_rect)
                    free_color_range=4
                elif hsv_hue[0][0][0] >64 and hsv_hue[0][0][0]<=80: #G3
                    screen.blit(g3_pygame,g3_rect)
                    free_color_range=5
                elif hsv_hue[0][0][0] >80 and hsv_hue[0][0][0]<=94:     #B1
                    screen.blit(b1_pygame,b1_rect)
                    free_color_range=6
                elif hsv_hue[0][0][0]>94 and hsv_hue[0][0][0]<=108:    #B2
                    screen.blit(b2_pygame,b2_rect)
                    free_color_range=7
                elif hsv_hue[0][0][0] >108 and hsv_hue[0][0][0]<=122:   #B3
                    screen.blit(b3_pygame,b3_rect)
                    free_color_range=8
                elif hsv_hue[0][0][0] >122 and hsv_hue[0][0][0]<=140:   #Purple
                     screen.blit(purple_pygame,purple_rect)
                     free_color_range=9
                elif hsv_hue[0][0][0] >140 and hsv_hue[0][0][0]<=150:   #purple/pink
                     screen.blit(purplepink_pygame,purplepink_rect)
                     free_color_range=10
                elif hsv_hue[0][0][0] >150 and hsv_hue[0][0][0]<=180:   #pink/red
                    screen.blit(pinkred_pygame,pinkred_rect)
                    free_color_range=11
                hue_screen=False
                
                pygame.display.flip()
            else:
                #find color of pick (x,y)
                # find fillColor
                if free_play ==True:
                    if free_color_range==0:
                        fillColor=reds[Ycoord,Xcoord]
                    elif free_color_range ==1:
                        fillColor=oranges[Ycoord,Xcoord]
                    elif free_color_range ==2:
                        fillColor = yellows[Ycoord,Xcoord]
                    elif free_color_range ==3:
                        fillColor = g1[Ycoord,Xcoord]
                    elif free_color_range ==4:
                         fillColor = g2[Ycoord,Xcoord]
                    elif free_color_range==5:
                        fillColor = g3[Ycoord,Xcoord]
                    elif free_color_range==6:
                        fillColor = b1[Ycoord,Xcoord]
                    elif free_color_range==7:
                        fillColor = b2[Ycoord,Xcoord]
                    elif free_color_range ==8:
                        fillColor = b3[Ycoord,Xcoord]
                    elif free_color_range==9:
                        fillColor = purple[Ycoord,Xcoord]
                    elif free_color_range==10:
                        fillColor = purplepink[Ycoord,Xcoord]
                    elif free_color_range==11:
                        fillColor = pinkred[Ycoord,Xcoord]
                    else:
                        fillColor = grey[Ycoord,Xcoord]
                else:
                    if color_range==0:
                        fillColor=reds[Ycoord,Xcoord]
                    elif color_range ==1:
                        fillColor=oranges[Ycoord,Xcoord]
                    elif color_range ==2:
                        fillColor = yellows[Ycoord,Xcoord]
                    elif color_range ==3:
                        fillColor = g1[Ycoord,Xcoord]
                    elif color_range ==4:
                         fillColor = g2[Ycoord,Xcoord]
                    elif color_range==5:
                        fillColor = g3[Ycoord,Xcoord]
                    elif color_range==6:
                        fillColor = b1[Ycoord,Xcoord]
                    elif color_range==7:
                        fillColor = b2[Ycoord,Xcoord]
                    elif color_range ==8:
                        fillColor = b3[Ycoord,Xcoord]
                    elif color_range==9:
                        fillColor = purple[Ycoord,Xcoord]
                    elif color_range==10:
                        fillColor = purplepink[Ycoord,Xcoord]
                    elif color_range==11:
                        fillColor = pinkred[Ycoord,Xcoord]
                    else:
                        fillColor = grey[Ycoord,Xcoord]
                fillB = int(fillColor[0])
                fillG = int(fillColor[1])
                fillR = int(fillColor[2])
                if color_range ==0:             #RED
                    cv2.drawContours(canvas, [contours_Red[shape_num]], -1, (fillB,fillG,fillR),thickness=-1)
                elif color_range ==1:           #ORANGE
                    cv2.drawContours(canvas, [contours_Orange[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==2:           #YELLOW
                    cv2.drawContours(canvas, [contours_Yellow[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==3:           #G1
                    cv2.drawContours(canvas, [contours_G1[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==4:           #G2
                    cv2.drawContours(canvas, [contours_G2[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==5:           #G3
                    cv2.drawContours(canvas, [contours_G3[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==6:           #B1
                    cv2.drawContours(canvas, [contours_B1[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==7:          # B2
                    cv2.drawContours(canvas, [contours_B2[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==8:           #B3
                    cv2.drawContours(canvas, [contours_B3[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==9:           #PURPLE
                    cv2.drawContours(canvas, [contours_Purple[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==10:          #PURPLE/PINK
                    cv2.drawContours(canvas, [contours_PurpPink[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range ==11:          #PINK/RED
                    cv2.drawContours(canvas, [contours_PinkRed[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                elif color_range==12:      #GREY
                    cv2.drawContours(canvas, [contours_Grey[shape_num]], -1,  (fillB,fillG,fillR),thickness=-1)
                if color_range <13:
                    draw_screen = True
                    cv2.drawContours(canvas, contours_all[12], -1, (0,0,0), thickness = 1)
                    cv2.drawContours(canvas, contours_all[13], -1, (0,0,0), thickness = -1)

                    cv2.imwrite('canvas.png',canvas)
                    canvasPygame = pygame.image.load("canvas.png")
                    canvas_rect = canvasPygame.get_rect()
                    screen.fill(BLACK)
                    screen.blit(canvasPygame ,canvas_rect)
                    pygame.display.flip()
                canvas_screen = not canvas_screen

GPIO.cleanup()

