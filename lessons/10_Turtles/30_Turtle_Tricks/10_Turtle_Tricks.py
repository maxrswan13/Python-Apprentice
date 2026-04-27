"""
For this program, you will tell Tina the Turtle to draw a triangle.

You should look at the previous programs to see how to use the turtle commands.
Copy lines of code from those programs to this one to draw a triangle.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

                 # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(1.5)                           # Make the turtle move as fast, but not too fast.

##
## Move Tina to the Starting Position
#

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-100, 100)                    # Move tina to the starting position
tina.pendown()                          # Put the pen down so we can draw

##
## Draw a triangle
##

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(200)                       # Move tina forward by the forward distance
tina.right(120)                          # Turn tina right a quarter turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(200)                       # Continue the last two steps three more times
tina.right(120)                          # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(200)
tina.right(120)



tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-50, -150)
tina.forward(20)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("RAHHHH RAHHHHH RAHHHHH RAHHHHHHH RRRAAAHHH RAAHHHHHH!!!!!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

turtle.exitonclick() # Use tina.forward() and tina.left() to draw a triangle
# Make each side of the triangle a different color with 
# tina.pencolor()

... # Your code here

turtle.exitonclick()                    # Close the window when we click on it