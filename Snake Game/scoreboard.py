from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.goto(0,270)
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.write(f"score = {self.count}",align="center",font=('Arial', 15, 'normal'))
      
        
    def counter(self):
        self.count+=1
        self.clear()
        self.write(f"score = {self.count}",align="center",font=('Arial', 15, 'normal'))
        
    def game_over(self):
        
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=('Arial', 15, 'normal'))
        