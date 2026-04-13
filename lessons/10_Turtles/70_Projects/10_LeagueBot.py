""" 
LeagueBot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bot.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 
"""

def set_turtle_image(tt, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent.parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    tt.shape(image_path)

import turtle as turtle

screen = turtle.Screen()
screen.setup(600, 600,0,0)
screen.bgcolor('white')

t = turtle.Turtle()
t.penup()
t.shape("turtle")

t.turtlesize(stretch_wid=5, stretch_len=5, outline=4)
set_turtle_image(t,"boy_yellow.gif")


def draw_polygon(sides):

    angle = 360/sides # Calculate angle from number of sides
    
    for i in range(sides):                 # Loop through the number of sides
        t.forward (100)                             # Move tina forward by the forward distance
        t.left (angle)                             # Turn tina left by the left turn

t.goto(-50,-50)
t.pendown()
t.color('blue')

draw_polygon(6)

turtle.exitonclick() # Your Code Here

