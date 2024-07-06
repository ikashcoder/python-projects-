from turtle import Turtle,Screen
from snake import Sanke
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Python Snake")
screen.tracer(0)


snake=Sanke()
food =Food()
sb =Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on=True

counter = 0

while game_on:
    if counter>0 or counter <3:
        time.sleep(0.8)
    elif counter>3 or counter<8:
        time.sleep(0.5)
    elif counter>8:
        time.sleep(0.3)
    screen.update()
    snake.move()
   

    if snake.head.distance(food) <15:
        food.refresh()
        sb.counter()
        snake.add_snake()
        counter+=1

    if snake.head.xcor()>295 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-290:
        game_on=False
        sb.game_over()
        
    for segment in snake.block_snake[1:]:
        
        if snake.head.distance(segment) <10:
            game_on=False
            sb.game_over()
        

screen.exitonclick()