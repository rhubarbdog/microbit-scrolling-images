#
# scroll.py - scroll images and text at any orienation
# Author - Phil Hall, August 2018  
from microbit import Image, display, sleep

def _validate_message(message):
    if not isinstance(message, (str, list, tuple)):
        raise TypeError('argument must be a string, list or tuple.')

    if type(message) is str:
        message=(message)
        
    for m in message:
        if not (type(m) is str or type(m) == type(Image.HEART)):
            raise TypeError('message can only contain text and images.')
    
def _message2images(message):

    if type(message) is str:
        message=(message)
        
    for gliph in message:

        if type(gliph) is str:
            for char in gliph:
                yield Image(char)
                
        else:
            yield gliph

def rotate_image(image,clockwise=True):

    if type(Image.HEART) != type(image):
        raise TypeError("argument must be an Image.")

    return _rotate_image(image,clockwise)

def _rotate_image(image,clockwise=True):
    new=Image(5,5)

    for y in range(5):
        for x in range(5):
            if clockwise:
                new.set_pixel(4-y,x,image.get_pixel(x,y))
            else:
                new.set_pixel(y,4-x,image.get_pixel(x,y))

    return new

def reflect_image(image,in_x=True):

    if type(Image.HEART) != type(image):
        raise TypeError("argument must be an Image.")

    return _reflect_image(image,in_x)

def _reflect_image(image,in_x=True):
    new=Image(5,5)
    for y in range(5):
        for x in range(5):
            if in_x:
                new.set_pixel(x,4-y,image.get_pixel(x,y))
            else:
                new.set_pixel(4-x,y,image.get_pixel(x,y))

    return new

def _show(image,delay):
    display.show(image,clear=False,wait=False)
    sleep(delay)
    
def _analyse_image(image):

    # handle single quote as special case otherwise '' looks like "
    if str(image) == str(Image("'")):
        return (0,3)
    
    left=None
    right=None
    skip=0
    for x in range(5):
        for y in range(5):
            if image.get_pixel(x,y)!=0:
                left=skip
                break

        if left is not None:
            break
            
        skip+=1
        
    if left is None:
        left=5

    skip=0
    for x in reversed(range(5)):
        for y in range(5):
            if image.get_pixel(x,y)!=0:
                right=skip
                break

        if right is not None:
            break
            
        skip+=1

    if right is None:
        right=5

    return (left,right)

def scroll_up(message,delay=150,scroll_down=False,monospace=False):

    if not display.is_on():
        return None
    
    err=False
    try:
        _validate_message(message)
    except TypeError as err_txt:
        save=err_txt
        err=True
    
    if err:
        raise TypeError(save)
    
    blank=Image(5,5)
    current=blank

    for pic in _message2images(message):

        if monospace:
            top=0
            bottom=0
        else:
            top,bottom=_analyse_image(pic)
            if top == 5:
                top=0
                bottom=4

        pic=_rotate_image(pic,not scroll_down)
        if scroll_down:
            pic=_reflect_image(pic)

        for row in range(top,5-bottom):
            if scroll_down:
                current=current.shift_down(1)
                current.blit(pic,0,row,5,1,0,0)
            else:
                current=current.shift_up(1)
                current.blit(pic,0,row,5,1,0,4)

            _show(current,delay)
            
        if scroll_down:
            current=current.shift_down(1)
            current.blit(blank,0,row,5,1,0,0)
        else:
            current=current.shift_up(1)
            current.blit(blank,0,row,5,1,0,4)

        _show(current,delay)

    for row in range(5):
        if scroll_down:
            current=current.shift_down(1)
            current.blit(blank,0,0,5,1,0,0)
        else:
            current=current.shift_up(1)
            current.blit(blank,0,0,5,1,0,4)

        _show(current,delay)

def scroll(message,delay=150,upside_down=False,monospace=False):
    
    if not display.is_on():
        return None
    
    err=False
    try:
        _validate_message(message)
    except TypeError as err_txt:
        save=err_txt
        err=True
    
    if err:
        raise TypeError(save)

    blank=Image(5,5)
    current=blank

    for pic in _message2images(message):

        if monospace:
            left=0
            right=0
        else:
            left,right=_analyse_image(pic)
            if left == 5:
                left=0
                right=4
            
        if upside_down:
            pic = _rotate_image(_rotate_image(pic))

        for col in range(left,5-right):

            if upside_down:
                current=current.shift_right(1)
                current.blit(pic,4-col,0,1,5,0,0)
            else:
                current=current.shift_left(1)
                current.blit(pic,col,0,1,5,4,0)

            _show(current,delay)

        if upside_down:
            current=current.shift_right(1)
            current.blit(blank,0,0,1,5,0,0)
        else:
            current=current.shift_left(1)
            current.blit(blank,0,0,1,5,4,0)

        _show(current,delay)

    for col in range(5):
        if upside_down:
            current=current.shift_right(1)
            current.blit(blank,0,0,1,5,0,0)
        else:
            current=current.shift_left(1)
            current.blit(blank,0,0,1,5,4,0)

        _show(current,delay)
