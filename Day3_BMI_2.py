print("This tool tell your BMI according to your Waight and hight \n")

hight =float(input("Enter your hight in Feet \n"))
weight =float(input("Enter your Weight in kg \n"))



BMI =weight/(hight/3.281)**2

print("Your Body Mass Index is : ",round(BMI,2))

if BMI <=18.5 :
    print("You are slightly Underweight \n")  
elif BMI<=25:
    print("You are at normal weight\n ")  
elif BMI<=30:
    print("You are Overweight \n")
elif BMI<=35:
    print("You are Obese \n")  
else:
    print("You are Clinically Obese \n")




    
    


