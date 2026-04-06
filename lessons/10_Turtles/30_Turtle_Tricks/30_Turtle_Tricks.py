"""
For this program, you will tell Tina the Turtle to draw 
multiple shapes.

Draw two circles, filled with different colors, 
and in different places on the screen. 

You should look at the previous program, 02_Meet_TIna.py
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
tina.speed(1.75)                           # Make the turtle move as fast, but not too fast.

##
## Move Tina to the Starting Position
#

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-10, 10)                    # Move tina to the starting position
tina.pendown()                          # Put the pen down so we can draw

##
## Draw a Square
##

tina.penup()     
tina.goto(-10, 10)
tina.pendown()     

tina.pendown()
tina.color('green')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(50)
tina.end_fill()
##
## Draw a Circle
##

tina.penup()     
tina.goto(-10, -150)
tina.pendown()     

tina.pendown()
tina.color('blue')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(50)
tina.end_fill()

##
## Write a Message
##

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(40, 40)
tina.forward(20)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("I am turtle")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

turtle.exitonclick()                    # Close the window when we click on it  

# You're on your way, soon you'll be writing your own programs!
# But first, let's save your progress. Continue with 
# the next file, 03_Check_In_Your_Code.ipynb# Use tina.circle() to draw a circle, and tina.goto() to move tina to a new location
# Use tina.begin_fill(), tina.end_fill(), and tina.fillcolor() to fill in the shapes

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it

# Dont forget to check in your code!