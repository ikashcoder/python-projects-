from turtle import Turtle,Screen
from paddle import Paddle


screen =Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.listen()

# tomTurtle =Turtle("square")
# tomTurtle.shapesize(6,1)
# tomTurtle.penup()
# tomTurtle.goto(350,0)
# tomTurtle.color("white")
tomTurtle = Paddle(350)

def move_up():
    y_cor = tomTurtle.ycor()+20
    tomTurtle.goto(tomTurtle.xcor(),y_cor)

def move_down():
    y_cor = tomTurtle.ycor()-20
    tomTurtle.goto(tomTurtle.xcor(),y_cor)
    

screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.exitonclick()