from turtle import Turtle

class Paddle :
    
    def __init__(self,x_cor):
        self.x_cor=x_cor
        self.make_paddle()
    
    def make_paddle(self):
        tomTurtle =Turtle("square")
        tomTurtle.shapesize(6,1)
        tomTurtle.penup()
        tomTurtle.goto(self.x_cor,0)
        tomTurtle.color("white")
    