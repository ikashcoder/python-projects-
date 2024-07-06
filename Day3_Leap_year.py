print("This is Leap Year Finder toll !!!")

year=int(input("Enter your year \n"))

if year%4==0:
    if year%100!=0:
            print(f"{year}: is Leap year ! \n")  
    else :
        if year%400==0:
            print(f"{year}:is Leap year ! \n")         
        else:
            print(f"{year}: This is not Leap year \n")
            
else:
            print("This is not Leap year \n")