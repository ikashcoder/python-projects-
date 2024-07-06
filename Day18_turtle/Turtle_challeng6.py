from turtle import Turtle,Screen,colormode
import random

tom =Turtle()

tom.pensize(2)
colormode(255)
def Randcolor():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    return (r,g,b)


tom.speed("fastest")

def spiroGraph(circle_tilt):
    for i in range(int(360/circle_tilt)):
        tom.circle(100)
        current_heading =tom.heading()
        tom.setheading(current_heading+circle_tilt)
        tom.pencolor(Randcolor())
    
    
spiroGraph(10)
    
screen =Screen()
    
screen.exitonclick()