import os
bidding_is_complete=False
Auction={} 
def Winner(bidding):
    Highest=0
    Winner=""
    for Bidder in bidding:
        Ammount =bidding[Bidder]
        if Ammount>Highest:
            Highest=Ammount
            winner=Bidder    
    print(f"The winner of Bidding is {winner} and ammount is {Highest}\n")

while not bidding_is_complete:
    name=input("Enter Your Name \n")
    Bid=int(input("Enter Your Bid in $ \n"))
    

    Auction[name]=Bid
    
    condition =input('Is there anyone else then Type "Yes" otherwise "No" \n').lower()
    
    if condition=="yes":
        os.system('cls')
    elif condition=="no":
        bidding_is_complete=True
        Winner(Auction)

    else :
        print("wrong input")
        