print("Pizzzza Order !!!")

size=input("What size pizza do you want ?? for small type 'S' medium 'M' Large 'L' \n")
peporani=input("Do you wnat peporoni ?? Y or N :")
chees=input("Do you wnat extra chess ?? Y or N : ")

bill=0

if size=='S':
    bill=15
    if peporani=='Y':
        bill+=2
elif size=='M':
    bill=20
    if peporani=='Y':
        bill+=3
elif size=='L':
    bill=25
    if peporani=='Y':
        bill+=3
else :
    print("Wrong Input !!! \n ")
    
if chees=='Y':
    bill+=1

print(f"Your Bill sir : ${bill}")