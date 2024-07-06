import random
from Day14_Temp import Actors
import os


def comparism(firstOne,secondOne,choise):
    if float(firstOne)<=float(secondOne) and choise =="b":
        print("You are right")
        return True
    elif float(firstOne)>=float(secondOne) and choise =="a":
        print("You are right")
        return True
    else:
        return False

print("<< This is higher Lower guessing game >>")
f_Actor =random.choice(list(Actors.keys()))

listActors =[]


score =0
boolbool =True
while(boolbool):

    s_Actor =random.choice(list(Actors.keys()))

    print(f"Compare A : {f_Actor} \n")
    print(f"Compare B : {s_Actor} \n")

    Check =input("Who has more rating : type 'A' or 'B' \n").lower()

    boolbool = comparism(Actors[f_Actor],Actors[s_Actor],Check)
    if boolbool ==True:
        score+=1
        f_Actor=s_Actor
    else:
        print(f"You lost and your score is {score}")
        
    