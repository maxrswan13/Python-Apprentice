# Tash Me with a Click
# 
# Update your Tash Me program ( copy your old program here ) to put 
# the moustache where you click on the screen.
#
# Hint: See 08a_More Turtle Programs, section 'Click on the Screen'
 
... # Your code here
import turtle

def set_background_image(window, image_name):
    """Set the background image of the turtle window to the image with the given name."""

    from pathlib import Path
    from PIL import Image

    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=10, starty=10)
    window.bgpic(image_path)

import turtle# Set up the screen                           # Tell Python we want to work with the turtle
turtle.setup(600, 600,0,0)     # Set the size of the window

tina = turtle.Turtle()  
                # Create a turtle named tina
screen = turtle.Screen()                # Get the screen that tina is on
set_background_image(screen, "emoji.png") # Set the background image of the screen

t = turtle.Turtle()
t.penup()
("moustache1.gif")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

def set_turtle_image(tt, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    tt.shape(image_path)

def turtle_clicked(t, x, y):

    print('turtle clicked!')
    
    for i in range(0,360, 20):
        t.tilt(20)

t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.exitonclick()
