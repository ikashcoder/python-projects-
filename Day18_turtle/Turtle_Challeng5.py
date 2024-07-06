from turtle import Turtle,Screen,colormode
import random 

tom =Turtle()
colormode(255)
def Randcolor():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    return (r,g,b)

tom.pensize(15)
tom.speed("fastest")


directions =[0,90,180,270]

for i in range(200):
  
    angle= random.choice(directions)
    tom.color(Randcolor())
    tom.forward(30)
    tom.left(angle)

sc =Screen()
sc.exitonclick()