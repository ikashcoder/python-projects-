def cypher_code(text,gap,choise):
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if gap>=len(letters):
        gap=gap%len(letters) 
    code=""
    if choise=="decode":
        gap*=-1  
    for single_char in text:
        if single_char not in letters:
            code+=single_char
        else:
            position =letters.index(single_char)
            position+=gap
            
            if position>=len(letters):
                position-=len(letters)
                code+=letters[position]
            else:
                code+=letters[position]
    print(f"The {choise}d massage is {code}")
        

condition =True

while condition :
    choise =input('Enter "Encode" for encoding the massage or Enter "Decode" for decoding the massage :').lower()
    if choise=="encode" or choise=="decode":
        msg =input("Enter the massage whitch do you want to encode :").lower()
        given_space =int(input("How much padding do you wann give :"))
        cypher_code(msg,given_space,choise)
        
        chalu_ya_band=int(input('Enter "1" for continue or "0" for stop :'))
        if chalu_ya_band== 0:
            condition=False

    
    



