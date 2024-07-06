
print("This is The challange to convert the 20$ into 54000 $ \n")


Day=1
ammount=10
risk=0
profit=0
lot=0


print("Day    Ammount      risk(20 pip)     lot sie      profit on 20 pip \n")
while(Day<30):
     risk=(ammount*30)/100  
     
     lot=risk/200
     profit=lot*200
     
     print(f"{Day}         {ammount:.2f}$         {risk:.2f}$         {lot:.2f}      {profit:.2f}$ ")
     ammount+=profit
     Day+=1
     
            
   
            
        