from microbit import Image, display, sleep

def _message2images(message):

    if not isinstance(message, (str, list, tuple)):
        raise TypeError('argument must be a string, list or tuple.')

    if type(message) is str:
        message=(message)
        
    result=[]

    for m in message:
        if type(m) is str:
            l=len(m)
        elif type(m) == type(Image.HEART):
            l=None
        else:
            raise TypeError('message can only contain text and images.')

        if l is None:
            result.append(m)
        else:
            for char in m:
                m=Image(char)
                result.append(m)

    return result

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

def scroll_up(message,delay=150,scroll_down=False,monospace=False):

    def analyse_image(image):
        rows=reversed(range(5))

        skip=0
        for y in rows:
            for x in range(5):
                if image.get_pixel(x,y)!=0:
                    return skip
            skip+=1

        return 5

    if not display.is_on():
        return None
    
    err=False
    try:
        images=_message2images(message)
    except TypeError as err_txt:
        save=err_txt
        err=True
    
    if err:
        raise TypeError(save)
    
    for i in range(len(images)):
        new=_rotate_image(images[i],not scroll_down)
        if scroll_down:
            new=_reflect_image(new)
        images[i]=new

    blank=Image(5,5)
    current=blank

    for pic in images:

        if monospace:
            skip=0
        else:
            skip=analyse_image(pic)
            if skip == 5:
                skip=4

        for row in range(5-skip):
            if scroll_down:
                current=current.shift_down(1)
                current.blit(pic,0,row,5,1,0,0)
            else:
                current=current.shift_up(1)
                current.blit(pic,0,row,5,1,0,4)

            display.show(current,clear=False,wait=False)
            sleep(delay)

        if scroll_down:
            current=current.shift_down(1)
            current.blit(blank,0,row,5,1,0,0)
        else:
            current=current.shift_up(1)
            current.blit(blank,0,row,5,1,0,4)

        display.show(current,clear=False,wait=False)
        sleep(delay)

    for row in range(5):
        if scroll_down:
            current=current.shift_down(1)
            current.blit(blank,0,0,5,1,0,0)
        else:
            current=current.shift_up(1)
            current.blit(blank,0,0,5,1,0,4)

            display.show(current,clear=False,wait=False)
            sleep(delay)
    

def scroll(message,delay=150,upside_down=False,monospace=False):
    
    def analyse_image(image,left2right=False):
        columns=range(5)
        if not left2right:
            columns=reversed(columns)

        skip=0
        for x in columns:
            for y in range(5):
                if image.get_pixel(x,y)!=0:
                    return skip
            skip+=1

        return 5

    if not display.is_on():
        return None
    
    err=False
    try:
        images=_message2images(message)
    except TypeError as err_txt:
        save=err_txt
        err=True
    
    if err:
        raise TypeError(save)

    if upside_down:
        for i in range(len(images)):
            images[i] = _rotate_image(_rotate_image(images[i]))

    blank=Image(5,5)
    current=blank

    for pic in images:

        if monospace:
            skip=0
        else:
            skip=analyse_image(pic,upside_down)
            if skip == 5:
                skip=4

        for col in range(5-skip):

            if upside_down:
                current=current.shift_right(1)
                current.blit(pic,4-col,0,1,5,0,0)
            else:
                current=current.shift_left(1)
                current.blit(pic,col,0,1,5,4,0)

            display.show(current,clear=False,wait=False)
            sleep(delay)


        if upside_down:
            current=current.shift_right(1)
            current.blit(blank,0,0,1,5,0,0)
        else:
            current=current.shift_left(1)
            current.blit(blank,0,0,1,5,4,0)

        display.show(current,clear=False,wait=False)
        sleep(delay)


    for col in range(5):
        if upside_down:
            current=current.shift_right(1)
            current.blit(blank,0,0,1,5,0,0)
        else:
            current=current.shift_left(1)
            current.blit(blank,0,0,1,5,4,0)

        display.show(current,clear=False,wait=False)
        sleep(delay)

