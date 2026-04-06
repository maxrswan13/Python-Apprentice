"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.

##
## Move Tina to the Starting Position
#

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-100, 100)                    # Move tina to the starting position
tina.pendown()                          # Put the pen down so we can draw

##
## Draw a Square
##

tina.pencolor('red')                   # Set the pen color to blue
tina.forward(200)                       # Move tina forward by the forward distance
tina.right(72)                          # Turn tina right a quarter turn

tina.pencolor('yellow')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(72)                          # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(200)
tina.right(72)

tina.pencolor('cyan')                 # Set the pen color to purple
tina.forward(200)
tina.right(72)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(200)
tina.right(72)


##
## Write a Message
##

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-60, -50)
tina.forward(20)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("Hi there!!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

turtle.exitonclick() # Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it