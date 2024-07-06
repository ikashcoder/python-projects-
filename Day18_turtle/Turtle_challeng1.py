from turtle import Turtle ,Screen


timmy =Turtle()
timmy.pencolor("blue")

def walk():
    timmy.forward(100)
    timmy.right(90)



for i in range(0,4):
    walk()




screen =Screen()
screen.exitonclick()

