from turtle import Turtle,Screen
from random import choice

tom =Turtle()

tom.pensize(15)
tom.speed("fastest")

colors =["dark blue","teal","crimson","magenta","dark slate blue","dark cyan","black","yellow"]

directions =[0,90,180,270]

for i in range(200):
    col =choice(colors)
    angle=choice(directions)
    tom.color(col)
    tom.forward(30)
    tom.left(angle)

sc =Screen()
sc.exitonclick()