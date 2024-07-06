def prime(number):
    count=0
    if number==1:
        print("1 is not either prime or not whole")
    else:
        for i in range(2,number+1):
            if number%i==0:
                count+=1
        if count==1:
            print(f"{number} it is prime number .")
        else:
            print(f"{number} it is whole number .")
            
        
        


num =int(input("Enter here number for checking it is \n*Prime number* \nor \n*whole number* :"))

prime(num)