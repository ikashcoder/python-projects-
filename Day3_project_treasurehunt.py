import random 

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Akash]
******************************************************************************* ''' )

print("*** Welcome To Treasure Hunt ***")
print("$ Your Mission is to solve problem and find treasure $")

first_no = random.randint(1,99)
second_no =random.randint(1,99)



key =int(input(f'''If you want to enter in your game u have to find key ...
        so key is the Answer of : {first_no} + {second_no} = '''))

ans =first_no+second_no

if key==ans:
    print("<- Now you are enter in the game -> ")
    accept=(input("Are you ready for the next challeges -- hit 'yes' for the proceed : ")).lower()
    
    if "yes"==accept:
        
        choise=int(input('''
                Chose right number :
                1 --->Go from Airoplane !!!
                2 --->Go from Boat !!!
                3 --->Go on the Bridge !!!
                4 --->Go By the road !!!
                
                '''))
        if choise==1:
                choise2=int(input('''Now You are in the plane ....
                      Chose right Number :
                      1 ---> Jump on the island when it comes ***/
                      2 ---> Don't jump and stay inside  ***/
                      
                      '''))

                if choise2 ==1:
                         cave=int(input('''Now you are on the island ....
                              Chose right number :
                              1 ---> White cave  ***/
                              2 ---> Yellow cave  ***/
                              3 ---> Red cave ***/
                
                              '''))
                         if cave==1:
                                print('''***Welcome treasure is here ***
                                      celebrate you got treasure ...
                                      (* Game End *)
                                      
                                      ''')
                         elif cave==2:
                                 print("You got wrong cave !!! (* Game End *)")
                                 
                         elif cave==3:
                                print("You got wrong cave !!! (* Game End *)") 
                         else:
                                print("You chosen violance and you were killed !!!(* Game End *)\n") 
                elif choise2==2:
                        print("Sorry you are no more because Your plane is crashed !!!  (* Game End *)\n")
                else:
                         print("You chosen violance and you were killed !!!(* Game End *)\n")         
                        
                
        elif choise==2:
                
                 boatchoise =int(input('''*** Now you are on the boat ***
                                      water flow of river is so fast choise is your ...
                                      chose right number :
                                      1 ---> Jump from the boat and go by swim /&
                                      2 ---> Stay in the boat /&
                                      
                                      '''))
                
                 if boatchoise==1:
                         print("In the water there are crocs so you are dead !!!(* Game End *)")
                         
                 elif boatchoise==2 :
                         cave2=int(input('''Exlant ... Now you are on the island ....
                              Chose right number :
                              1 ---> White cave  ***/
                              2 ---> Yellow cave  ***/
                              3 ---> Red cave ***/ '''))
                         if cave2==1:
                                print('''***Welcome treasure is here ***
                                      celebrate you got treasure ...
                                      (* Game End *)
                                      ''')
                         elif cave2==2:
                                 print("You got wrong cave !!! (* Game End *)")
                                 
                         elif cave2==3:
                                print("You got wrong cave !!! (* Game End *)") 
                         else:
                                print("You chosen violance and you were killed !!!(* Game End *)\n")      
                
                 else:
                        print("You chosen violance and you were killed !!!(* Game End *)\n")      
                
        elif choise==3:
                 bridgechoise =int(input('''*** Now you are on the bridge ***
                                      water flow of river is so fast ...
                                      But bridge is close to break do you want to take risk choise is your ...
                                      chose right number :
                                      1 ---> Jump from the Bridge and go by swim /^
                                      2 ---> Stay on the Bridge /^
                                      
                                      '''))
                
                 if bridgechoise==1:
                         print("In the water there are crocs so you are dead !!!(* Game End *)")
                         
                 elif bridgechoise==2 :
                         cave3=int(input('''Exlant ... Now you are on the island ....
                              Chose right number :
                              1 ---> White cave  ***/
                              2 ---> Yellow cave  ***/
                              3 ---> Red cave ***/ '''))
                         if cave3==1:
                                print('''***Welcome treasure is here ***
                                      celebrate you got treasure ...
                                      (Game End )
                                      
                                      ''')
                         elif cave3==2:
                                 print("You got wrong cave !!! (* Game End *)")
                                 
                         elif cave3==3:
                                print("You got wrong cave !!! (* Game End *)") 
                         else:
                                print("You chosen violance and you were killed !!!(* Game End *)\n")      
                
                 else:
                        print("You chosen violance and you were killed !!!(* Game End *)\n")      
                
        elif choise==4:
                print("***Sorry to say but you chose wrong way for Trasure hunt and you go opposite in the direction so Game is End ****")
        else:
                print("You chosen violance and you were killed !!!(* Game End *)\n")
                
else:
                print("You chosen violance and you were killed !!!(* Game End *)\n")
        
                
            
            
                
                
            
    
    