import turtle

# Create the screen and the turtle
screen = turtle.Screen()
t = turtle.Turtle()

# Define functions for moving the turtle
def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.left(30)

def turn_right():
    t.right(30)

def change_color():
    t.color("blue")

def pen_up():
    t.penup()

def pen_down():
    t.pendown()

def exit_program():
    screen.bye()

# Set up the screen to listen for key presses
screen.listen()

# Bind letter keys to functions
screen.onkey(move_forward, "w")  # 'w' key to move forward
screen.onkey(move_backward, "s") # 's' key to move backward
screen.onkey(turn_left, "a")     # 'a' key to turn left
screen.onkey(turn_right, "d")    # 'd' key to turn right
screen.onkey(change_color, "c")  # 'c' key to change color
screen.onkey(pen_up, "u")        # 'u' key to lift the pen up
screen.onkey(pen_down, "p")      # 'p' key to put the pen down
screen.onkey(exit_program, "q")  # 'q' key to exit the program

# Start the turtle graphics loop
turtle.mainloop()
