import random

print('*** This is coin toss tool ***')

toss=(input("Enter 'Toss' for toss \n")).lower()

flip=random.randint(0,1)



if toss=="toss":
    if flip==1:
        print("HEAD\n")
    else:
        print("TAIL\n")
        
else:
    print("Wrong Input !!!")