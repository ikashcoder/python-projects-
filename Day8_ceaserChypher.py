def encode(text,gap):
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if gap>=len(letters):
        gap=gap%len(letters)
        
    encode=[]
    for single_char in text:
        if single_char not in letters:
            encode+=single_char
        else:
            for position in range(len(letters)):
                letter =letters[position]
                if single_char==letter:
                    position+=gap

                    if position>=len(letters):
                        position-=len(letters)
                        encode+=letters[position]
                    else:
                        encode+=letters[position]
    for code in encode:
        print(code,end="")
    print("\n")
        
def decode(text,gap):
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if gap>=len(letters):
        gap=gap%len(letters)
    decode=[]
    for single_char in text:
        if single_char not in letters:
            encode+=single_char
        else:
            for position in range(len(letters)):
                letter =letters[position]
                if single_char==letter:
                    position-=gap
                    if position<0:
                        position+=len(letters)
                        decode+=letters[position]
                    else:
                        decode+=letters[position]
    for code in decode:
        print(code,end="")
    print("\n")
        

        

condition =True

while condition :
    choise =input('Enter "Encode" for encoding the massage or Enter "Decode" for decoding the massage :').lower()
    if choise=="encode":
        msg =input("Enter the massage whitch do you want to encode :").lower()
        given_space =int(input("How much padding do you wann give :"))
        encode(msg,given_space)
        
    elif choise=="decode":
        msg =input("Enter the massage whitch do you want to decode :").lower()
        given_space =int(input("How much padding do you wann give :"))
        decode(msg,given_space)

    chalu_ya_band=int(input('Enter "1" for continue or "0" for stop :'))
    if chalu_ya_band== 0:
        condition=False

    
    



