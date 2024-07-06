from turtle import Turtle,Screen

tim =Turtle()

def W_forward():
    tim.forward(10)
def S_backward():
    tim.backward(10)
def A_counter_clockwise():
    tim.left(10)
def D_clockwise():
    tim.right(10)
def C_clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()   




sc=Screen()
sc.listen()

sc.onkey(W_forward,"Up")
sc.onkey(S_backward,"Down")
sc.onkey(A_counter_clockwise,"Left")
sc.onkey(D_clockwise,"Right")
sc.onkey(C_clear,"c")

sc.exitonclick()