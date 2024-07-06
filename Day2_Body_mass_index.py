print("This tool tell your BMI according to your Waight and hight \n")

hight =input("Enter your hight in Feet \n")
weight =input("Enter your Weight in kg \n")



BMI =float(weight)/(float(hight)/3.281)**2

print("Your Body Mass Index is : " ,int(BMI))


