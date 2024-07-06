from turtle import Turtle


SATRTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Sanke:
    
    def __init__(self):
        self.block_snake=[]
        self.create_snake()
        self.head=self.block_snake[0]
        
    def create_snake(self):
        for position in SATRTING_POSITION:
          self.add_segment(position)
            
    def add_segment(self,position):
        new_blockof_snake=Turtle("square")
        new_blockof_snake.penup()
        new_blockof_snake.color("white")
        new_blockof_snake.goto(position)
        self.block_snake.append(new_blockof_snake)
    
    def add_snake(self):
        self.add_segment(self.block_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.block_snake)-1,0,-1):
            new_x=self.block_snake[seg_num-1].xcor()
            new_y =self.block_snake[seg_num-1].ycor()
            self.block_snake[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE)
       
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def left(self):
        if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT) 
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN) 
    def right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT) 
            
    
    