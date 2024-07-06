from turtle import Turtle,Screen

tom =Turtle()


def tringle():
    angle =360/3
    for i in range(3):
        tom.pencolor("gold1")
        tom.forward(100)
        tom.right(angle)

def squre():
    angle =360/4
    for i in range(4):
        tom.pencolor("brown")
        tom.forward(100)
        tom.right(angle)

def panta():
    angle =360/5
    for i in range(5):
        tom.pencolor("violet")
        tom.forward(100)
        tom.right(angle)

def hexa():
    angle =360/6
    for i in range(6):
        tom.pencolor("cyan")
        tom.forward(100)
        tom.right(angle)

def hepta():
    angle =360/7
    for i in range(7):
        tom.pencolor("black")
        tom.forward(100)
        tom.right(angle)

def ocata():
    angle =360/8
    for i in range(8):
        tom.pencolor("orange")
        tom.forward(100)
        tom.right(angle)
def nona():
    angle =360/9
    for i in range(9):
        tom.pencolor("green")
        tom.forward(100)
        tom.right(angle)

def deca():
    angle =360/10
    for i in range(10):
        tom.pencolor("yellow")
        tom.forward(100)
        tom.right(angle)


    

tringle()
squre()
panta()
hexa()
hepta()
ocata()
nona()
deca()







sc =Screen()
sc.exitonclick()