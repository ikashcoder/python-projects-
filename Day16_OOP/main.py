import turtle
import prettytable

timmy =turtle.Turtle()
timmy.shape("turtle")
timmy.color("green")

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        timmy.color(c)
        timmy.forward(steps)
        timmy.right(30)
        

my_screen =turtle.Screen()
my_screen.exitonclick()
