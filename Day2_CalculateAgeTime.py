

print("This is the calculator that tells you if u live till 90 years how many Days ,Weeks ,and Years do you have !!! ")
age =input("Enter your current age :")

Year_limit=90

Years= Year_limit - int(age)
Month =Years *12
Weeks=Years * 52
Days =Weeks *7

print(f"Your Remaining \n Years : {Years}\n Month : {Month} \n Weeks :{Weeks}\n Days :{Days}\n")




