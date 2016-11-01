import glib
def noisemaker3000 (x,y,freq,octaves):
    from noise import pnoise2
    value = pnoise2(x/freq, y/freq, octaves)
    return value
def powerswitch (bottom, top, value):
    a = (top-bottom)/2
    newvalue = (a*value)+(bottom+a)
    return newvalue
"""
Write another function that takes width, height, freq and octaves
and creates a list-of-lists where the number of lists is height and
each list has width Perlin Noise values scaled to be between 0 and 255.
Hint: use the first two functions to do this).
"""
def lister(x,y,freq,octaves):
    heit = []
    for i in range ( 0 , y):
        heit.append([])
        for j in range (0 , x):
            heit[i].append(i)
            heit[i].append(j)
            for q in range (0,3):
                kekr = powerswitch ( 0 , 255 , noisemaker3000 (i , j , freq , octaves))
                heit[i].append(kekr)
    return heit
                                      
    
def main ():
    import glib
    glib.open_window(800, 600)
    im = glib.create_image (750,550)
    model = glib.get_pixels (im)
    for x in range ( 0 , im.size[0]):
        for y in range (0 , im.size[1]):
            color = model.getpixel(x,y)
            model.setpixel(x, y, (150,200,200))
    """
    In your main function, use that third function to create a list-of-lists of noise values
    the same size as the image you created (use frequency 16.0 and octaves 1). Then, set the
    pixels in the image to the values in the list-of-lists. That is, for each pixel, set it to
    the RGB color (v,v,v) where v is the value in the list-of-lists at the same coordinates.
    Note that the RGB values need to be ints,
    so you'll have to convert from floats in the list-of-lists.
    """
    v = lister (im.size[0] , im.size[1] , 16.0 , 1)
    for h in range ( 0 , im.size[1]):
        for w in range (0 , im.size[0]):
            color = model.getpixel(w,h)
            new_pixel = v[h] 
            model.setpixel(w, h, (int(new_pixel[2]),int(new_pixel[3]),int(new_pixel[4])))
    
    glib.show_image(im, 400, 300)
    glib.update()

main()
