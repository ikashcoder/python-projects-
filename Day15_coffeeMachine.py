from coffeemachineRequrements import coffees
import os
print("**This Is the coffee Machine**")
sorage ={
    "Water" :500,
    "Coffee":30,
    "Milk" :500,
    "Balance":0
}

def coinCunting(coin1=0,coin2=0,coin5=0,coin10=0):
    Total =coin1+(coin2 *2)+(coin5*5)+(coin10 *10)
    return Total

def remainStorage(choise):
    sorage["Water"]=sorage["Water"]-coffees[choise-1]["Water"]
    sorage["Coffee"]=sorage["Coffee"]-coffees[choise-1]["Coffee"]
    sorage["Milk"]=sorage["Milk"]-coffees[choise-1]["Milk"]
    sorage["Balance"]=sorage["Balance"]+coffees[choise-1]["Price"]
    
def check():
    forContinue =input("Enter 'y' for continue or 'n' for exit here !").lower()       
    if forContinue=='n':
        conditon =False
    
    return conditon
 
conditon =True
    
while conditon:    
    choise =int(input('''
                    Enter 1 : Espresso 
                                price :10 $
                    Enter 2 : Latte 
                                price :15 $
                    Enter 3 : Cappuccino 
                                price :20 $
                    Enter 4 : Report             
                    '''))
    if choise in range(1,4):
        print(f" Your coffee is :{coffees[choise-1]["CoffeeName"]} \n and Price of your coffee is :{coffees[choise-1]["Price"]}")


        if sorage["Water"]>=coffees[choise-1]["Water"] and sorage["Coffee"]>=coffees[choise-1]["Coffee"]  and sorage["Milk"]>=coffees[choise-1]["Milk"]:
            
            coin1 =int(input("1 $ coins : "))
            coin2 =int(input("2 $ coins : "))
            coin5 =int(input("5 $ coins : "))
            coin10 =int(input("10 $ coins : "))

            total =coinCunting(coin1,coin2,coin5,coin10)


            
            if total >=coffees[choise-1]["Price"]:
                
                change =total-coffees[choise-1]["Price"]
                
                print(f"You give : {total} and here is your change : {change}\n")
                
                print("--Enjoy Your coffee ... *** HAVE A GOOD DAY ***")
                
                remainStorage(choise)
                conditon =check()
                os.system("cls")
            
            else :
                print(f"Insuff money ... your {total}$ is refundede !")
                conditon =check()
                os.system("cls")
                
        else :
            print(f'''\n Sorry for inconveniance we dont have that much material to create coffee :
                coffee powder : {sorage["Coffee"]} , Milk :{sorage["Milk"]}, Water :{sorage["Water"]}
                ''')
            conditon =check()
            os.system("cls")
            
    else:
        print(f'''
            coffee Powder :{sorage["Coffee"]} ,
            Milk :{sorage["Milk"]},
            Water :{sorage["Water"]}
            ''')
        conditon =check()
        os.system("cls")