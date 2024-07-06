import random

randomNumber =random.randint(1,100)


print("*/ Welcome to Number Guessing Game */ ")
level =int(input('''Chose Your level first
                1)Easy
                2)hard
                please type number respectivly whats level you want to chose ...
             '''))

def checkNum(yourNumber):
    if yourNumber < randomNumber:
        print("Higher number")
    elif yourNumber > randomNumber:
        print("Lower number")
 
if level==1:
    life=10
elif level ==2:
    life =5
else:
    print("Wrong Input")
    
        
for i in range(1,life):
    yourNumber =int(input("Enter your Guess : "))
    if yourNumber==randomNumber:
        print(f"{yourNumber} : is the right number you win with ({life - i }) lifes ")
        break
    checkNum(yourNumber)
    print(f"You have {life - i} lifes ")
    
    if life-i==0:
        print("You lose")