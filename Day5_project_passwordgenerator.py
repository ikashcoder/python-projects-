import random
print("this is password generstor !!!")

cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=[1,2,3,4,5,6,7,8,9,0]
symbols=['!','@','#','$','%','^','&','*','(',')']

lenght_of_pass=int(input("Enter the lenght of password\n")) #8

number_of_char=int(input("How many character do you want ??\n"))#2

numbers_of_numbers=int(input("How many Numbers do you want ??\n"))#4

numbers_of_symbols=int(input("How many Symbols do you want ??\n"))#2

letter=[]
number=[]
symbol=[]

if lenght_of_pass==number_of_char + numbers_of_numbers+numbers_of_symbols:

    if number_of_char!=0:
        for counter1 in range(0,number_of_char):
            rand_char=random.randint(0,len(cap_letters)-1)
            letter.append(cap_letters[rand_char])
        
    #print(letter)    
    if numbers_of_numbers!=0:
        for counter2 in range(0,numbers_of_numbers):
            rand_no=random.randint(0,len(numbers)-1)  
            number.append(numbers[rand_no])
    #print(number)    
    if numbers_of_symbols!=0:
        for counter3 in range(0,numbers_of_symbols):
            rand_sym=random.randint(0,len(symbols)-1)
            
            symbol.append(symbols[rand_sym])
    #print(symbol)
else :
    print("Length is not given in proper manner \n")
    
    
#password=[]

password=letter + number + symbol

#print(password)

random.shuffle(password)
    
for end_pass in password:
    
    print(end_pass,end='')
    
    
    
    
    
    
    
#)M8C8*%14YR8J)#