from microbit import *
import scroll

text=(Image.HAPPY," Hello world. ",Image.HAPPY)

while True:
    scroll.scroll(text)
    sleep(1000)
    scroll.scroll_up(text)
    sleep(1000)
    scroll.scroll(text,upside_down=True)
    sleep(1000)
    scroll.scroll_up(text,scroll_down=True)
    sleep(1000)
