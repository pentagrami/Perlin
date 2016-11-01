import glib
def intensity (x,y,freq,octaves):
    from noise import pnoise2
    value = pnoise2(x/freq, y/freq, octaves)
    return value
def decibel (bottom, top, value):
    a = (top-bottom)/2
    newvalue = (a*value)+(bottom+a)
    return newvalue
def cacophony(x,y,freq,octaves):
    noises = []
    for i in range ( 0 , y):
        noises.append([])
        for j in range (0 , x):
            note = decibel ( 0 , 255 , intensity (i , j , freq , octaves))
            noises[i].append([note])
    return noises
def remix (base , modifier):
    product = []
    for i in range ( 0 , len(base) ):
        product.append([])
        for j in range ( 0 , len(base[i])):
                         sound = ((base[i][j][0])+(modifier[i][j][0]))/2
                         product[i].append([sound])
    return product
def symphony (length, height, layers):
    beat = 16.0
    rhythm = cacophony (length , height , beat , 1)
    for i in range (0,layers):
        beat = beat * 2
        rhythm = remix ((rhythm),cacophony (length , height , beat , 1))
    return rhythm    
def main ():
    import glib
    glib.open_window(800, 600)
    im = glib.create_image (750,550)
    model = glib.get_pixels (im)
    length = im.size[0]
    height = im.size[1]
    for x in range ( 0 , length):
        for y in range (0 , height):
            color = model.getpixel(x,y)
            model.setpixel(x, y, (150,200,200))
    song = symphony (length, height, 4)
    for h in range ( 0 , height):
        for l in range (0 , length):
            color = model.getpixel(l,h)
            v = int(song[h][l][0])
            model.setpixel(l, h, (v,v,255))    
    glib.show_image(im, 400, 300)
    glib.update()
main()
