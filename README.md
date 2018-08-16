<html>
<body>
<big><big>Scroll - </big></big>scrolling text and images at any orientation.
</br></br>
Is your microbit always at the wrong angle when using microbit.display methods?
<code>scroll.py</code> could be the answer scroll combined images and text upside down, upwards or scroll down.</br></br>

There are 2 functions and 2 useful helper functions,</br></br>
<code>scroll(message,delay=150,upside_down=False,monospace=False)</code></br>
scrolls text and images horizontally, <i>message</i> can be a string, or a list/tuple of strings and images. <i>delay</i> controlls how fast the image scrolls.</br>
if <i>upside_down</i> is True then the text will be scrolled upside down.</br>
if <i>monospace</i> is True all text and images will be 5 pixels wide seperated by a sigle blank line. Otherwise images and characters have their right space trimmed leaving 1 maybe 2 pixels between each image.</br></br>
<code>scroll_up(message,delay=150,scroll_down=False,monospace=False)</code></br>
scrolls text and images vertically, by default messages scroll up. <i>message</i> can be a string, or a list/tuple of strings and images. <i>delay</i> controlls how fast the image scrolls.</br>
if <i>scroll_down</i> is True then the text will be scrolled down.</br>
if <i>monospace</i> is True all text and images will be 5 pixels wide seperated by a sigle blank line. Otherwise images and characters have their right space trimmed leaving 1 maybe 2 pixels between each image.</br></br>

both scroll functions wait until the animation is complete. Should the display be deactivated (microbit.display.is_on() is False) then nothing will be displayed, and the functions return immediately.</br></br>
There are 2 helper functions to manipulate images.</br>
<code>rotate_image(image,clockwise=True)</code> returns a new image rotated by 90 degrees. If <i>clockwise</i> is False then the image will be rotated anticlockwise.</br>
<code>reflect_image(image,in_x=True)</code> returns a new image reflected in either the x axis or when argument <i>in_x</i> is False then in the y axis.
</body>
</html>
