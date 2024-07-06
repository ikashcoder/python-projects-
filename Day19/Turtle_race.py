from turtle import Turtle,Screen
import random
import tkinter as tk
from tkinter import messagebox

screen =Screen()
screen.setup(width=500,height=400)



start_race =False
colors=["red","blue","yellow","green","orange","pink"]
y_cor=-100
all_turtles =[]
root = tk.Tk()
root.withdraw() 
for i in range(len(colors)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y=y_cor)
    y_cor+=30
    
    all_turtles.append(new_turtle)
    
bet_on_turtle=screen.textinput(title="Make Your Bet !",prompt="Whitch turtle will win the race ? Enter the colour : ")
    
if bet_on_turtle in colors:
    start_race=True
    
while start_race:
    
    for turtle in all_turtles:
        if turtle.xcor()>230:
            win_color =turtle.pencolor()
            if win_color ==bet_on_turtle:
             
                # Hide the main tkinter window
                messagebox.showinfo("Message", f"Your Turtle is Win ! and color of That Turtle is :{win_color}")
                
            else:
                messagebox.showinfo("Message", f"You lose ! And Winner Color of turtle is :{win_color}")
                
            root.destroy()
            start_race=False
        
        distance =random.randint(0,10)
        turtle.forward(distance)
        
screen.exitonclick()