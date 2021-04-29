def rgb_to_hsv1(r, g,b):
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
        s = (df/mx)*255
    v = mx*255
    h = h/2
    return h, s, v
#code_run=1
#while code_run
print('Red')
print(rgb_to_hsv1(255,153,153))
print(rgb_to_hsv1(153,0,0))
print('orange')
print(rgb_to_hsv1(255,204,153))
print(rgb_to_hsv1(153,76,0))
print('Y')
print(rgb_to_hsv1(255,255,153))
print(rgb_to_hsv1(153,153,0))
print('G1')
print(rgb_to_hsv1(204,255,153))
print(rgb_to_hsv1(76,153,0))
print('G2')
print(rgb_to_hsv1(153,255,153))
print(rgb_to_hsv1(0,153,0))
print('G3')
print(rgb_to_hsv1(153,255,204))
print(rgb_to_hsv1(0,153,76))
print('B1')
print(rgb_to_hsv1(153, 255, 255))
print(rgb_to_hsv1(0,153,153))
print('B2')
print(rgb_to_hsv1(153, 204, 255))
print(rgb_to_hsv1(0, 76, 153))
print('B3')
print(rgb_to_hsv1(153, 153, 255))
print(rgb_to_hsv1(0, 0, 153))
print('Purp')
print(rgb_to_hsv1(204, 153, 255))
print(rgb_to_hsv1(76, 0, 153))
print('Purp/Pink')
print(rgb_to_hsv1(255, 153, 255))
print(rgb_to_hsv1(153, 0, 153))
print('Pink/Red')
print(rgb_to_hsv1(255, 153, 204))
print(rgb_to_hsv1(153, 0, 76))
print('Grey')
print(rgb_to_hsv1(224, 224, 224))
print(rgb_to_hsv1(64, 64, 64))
