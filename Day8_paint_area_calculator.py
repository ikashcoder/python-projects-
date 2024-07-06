
import math

def paint_area_cal(hight,width,cover):
    paint_cans=((hight*width)/cover)
    ans=math.ceil(paint_cans)
    return ans

print("This tool provides you how much paint cans you need to paint your wall . (per 5 squre meter 1 can of paint )")

hight_of_wall=float(input("Enter the hight of wall in meter :"))
width_of_wall=float(input("Enter the width of wall in meter :"))
coverage=5

paint=paint_area_cal(hight_of_wall,width_of_wall,coverage)

print(f"You should use {paint} cans of paints !!!")