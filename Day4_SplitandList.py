import random

print("That is bill pay tool . Whoes name will be come he/she will pay the bill... ")
names=input("Enter all names and separate it with comma --> \n").split(",")

list_size=len(names)

#who_pay=random.choice(names)
who_pay=random.randint(0,list_size-1)
print(f"{names[who_pay]} , You are the lucky one ### You have pay the bill !")
