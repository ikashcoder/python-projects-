from turtle import Turtle,Screen

tom =Turtle()

colors =["dark blue","teal","crimson","magenta","dark slate blue","dark cyan","black","yellow"]

side =3
for j in range(8):
    angle =360/side
    for i in range(side):
        tom.pencolor(colors[j])
        tom.forward(100)
        tom.right(angle)
    side+=1
    
sc =Screen()
sc.exitonclick()