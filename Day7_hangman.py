import random
from Day7_hangman_Art import logo,lives
from Day7_hangman_wordList import words

print(logo)


       
rand_word=random.choice(words)
#print(rand_word)
display=[]

for _ in range(len(rand_word)):
     display+="_"
   
for j in range(len(rand_word)):        
    print(display[j],end=" ")
chance =6
condition=True

while(condition):
    choise =(input("\nGuess the letter of the word : ")).lower()
    
    if choise in display :
        print(f"You Again entered : {choise} ")
    else:
        for position in range(len(rand_word)):
            
            letter =rand_word[position]
            if choise==letter:
            
            
                display[position]=choise
        
        for j in range(len(rand_word)):        
            print(display[j],end=" ") 
        
        if "_" not in display:
            print("*** You win!!! ***")
            condition=False     
            
        if choise not in rand_word:
            chance-=1
        
                
        print(lives[chance])
        
        if chance==0:
            condition=False
            
   