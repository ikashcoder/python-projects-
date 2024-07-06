# import colorgram


# colour =colorgram.extract("image.jpg",30)

# rgb_colors=[]

# for color in colour:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
    
#     new_color =(r,g,b)
    
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

from turtle import Turtle,Screen,colormode
import random
colormode(255)

painting_colors=[(241, 228, 58), (220, 150, 79), (186, 67, 30), (234, 46, 112), (192, 12, 35), (40, 206, 88), (18, 19, 48), (40, 93, 171), (36, 34, 151), (233, 225, 5), (94, 186, 216), (66, 13, 43), (195, 39, 76), (200, 13, 7), (234, 61, 37), (51, 24, 13), (220, 161, 12), (217, 135, 180), (87, 209, 147), (25, 145, 35), (97, 235, 176), (13, 198, 217), (242, 159, 194), (94, 75, 12), (81, 85, 209), (13, 37, 30)]


tim =Turtle()
tim.hideturtle()
tim.speed("fastest")
tim.penup()
angle =(180+270)/2
tim.setheading(angle)
tim.forward(300)
tim.setheading(0)

for j in range(10):
    for i in range(10):
        tim.dot(15,random.choice(painting_colors))
        tim.forward(50)

    
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading(0)




screen =Screen()
screen.exitonclick()