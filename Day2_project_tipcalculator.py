print("Welcom to tip calculator !!! ")

bill =float(input("What is the Bill amount : $ "))

tip_per =int(input("How many tip do u want to give in percentage like 12 ,14 ,15 : "))

tip=tip_per*bill/100

last_bill =bill+tip

people =input("How many people to split the bill ")

each=round(last_bill/int(people),2)

print(f"Each person should pay {each} \n ")

