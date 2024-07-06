import random
import os

def winner(myhand,sum1,DealerHand,sum2):
    print(f"My Hand :{myhand} And Sum is :{sum1}")
    print(f"Dealer Hand :{DealerHand} And Sum is :{sum2}")
    if sum1<sum2:
        print("Dealer is win")
    elif sum1>sum2:
        print("You are win")
    else:
        print("The match is tie ")
       
play=True
 
while play:
    print('''
        _             _                                 _     
  _ __ | | __ _ _   _(_)_ __   __ _    ___ __ _ _ __ __| |___ 
 | '_ \| |/ _` | | | | | '_ \ / _` |  / __/ _` | '__/ _` / __|
 | |_) | | (_| | |_| | | | | | (_| | | (_| (_| | | | (_| \__ \\
 | .__/|_|\__,_|\__, |_|_| |_|\__, |  \___\__,_|_|  \__,_|___/
 |_|            |___/         |___/                           
          
          ''')
    print("Welcom to Blackjack !!!")

    cards=[11,2,3,4,5,6,7,8,9,10,10,10]

    myhand=[]
    DealerHand=[]
    sum1=0
    sum2=0


    for i in range(2):
        randomHand1 =random.randint(0,len(cards)-1)
        myhand.append(cards[randomHand1])
        randomHand2 =random.randint(0,len(cards)-1)
        DealerHand.append(cards[randomHand2])
        
    print(myhand)
    print(DealerHand[0])

    Option=input('Do you wnat to "Hit" or "Stand" !! type your option respectively:\n').lower()

    if Option =="hit":
        randomHand1 =random.randint(0,len(cards)-1)
        if randomHand1==0:
            if sum2>10:
                myhand.append(1)
        else:
            myhand.append(cards[randomHand1])
        Option="stand"  

    if Option=="stand":
    
        for number in myhand:
            sum1=sum1+number
        
        for number in DealerHand:
            sum2=sum2+number
            
        
        #print(sum1)
        #print(sum2)
        
        if sum1==21:
            print(f"My Hand : {myhand} And Sum is :{sum1}\n")
            print(f"Dealer Hand :{DealerHand} And Sum is :{sum2}\n")
            print("it's BlackJack. You Win !!!")
        elif sum1>21:
            print(f"My Hand : {myhand} And Sum is :{sum1}\n")
            print(f"Dealer Hand :{DealerHand} And Sum is :{sum2}\n")
            print("You Lose")
            
        else:
            if sum2==21:
                print("it's BlackJack. Dealer Win !!!")
            elif sum2<16:
                
                while sum2<16:
                    randomHand2 =random.randint(0,len(cards)-1)
                    if randomHand2==0:
                        if sum2>10:
                            DealerHand.append(1)
                            sum2=sum2+1
                    else:
                        DealerHand.append(cards[randomHand2])
                        sum2=sum2+cards[randomHand2]
                    
                    winner(myhand,sum1,DealerHand,sum2)
                    
            else:
                winner(myhand,sum1,DealerHand,sum2)
        ans=input('Do you wanna play again ?? if Yes type "Y" if no then type "N"').lower()
        
        if ans=="n":
            play=False
        else:
            os.system('clear')            
                
    else :
        print("Wrong input ??? ")                
        ans=input('Do you wanna play again ?? if Yes type "Y" if no then type "N"').lower()
        if ans=="n":
            play=False         