print('''

_____________________
|  _________________  |         
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|      
      
      
      ''')


def calci(No1,No2,Input):
    if Input=='+':
        Ans= No1+No2
    elif Input=='-':
        Ans= No1-No2
    elif Input=='*':
        Ans= No1*No2
    elif Input=='/':
        Ans= No1/No2

    return Ans

condition =True
Number1=0
Number2=0
Decesion='n'
while condition:
    operators =['+','-','*','/']  
    if Decesion=='n':  
        Number1=int(input("Enter your First Number :\n"))
    else:
        print(f"Previous Value is {Number1}")
        
    operator =input("Enter operator : \n+\n-\n*\n/\n")

    if operator not in operators:
        print("Wrong input ")

    else:
        Number2=int(input("Enter your Second Number :\n"))
        
        Answer=calci(Number1,Number2,operator)
        
        print(f"{Number1} {operator} {Number2}={Answer}")
        
        Decesion=input(f"Type 'y' to calculating with {Answer} or Type 'n' for calculating with new number for stoping the calculation type 's' \n").lower()
        
        if Decesion=='y':
            Number1=Answer
        elif Decesion=='s':
            condition =False
            
        
    