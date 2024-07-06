import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)                
---.__(___)

'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
game=[rock,paper,scissors]

choise=int(input('''This is Rock ,Paper ,Scissor game ###
                 Enter following number for choise :
                 1-->Rock
                 2-->Paper
                 3-->scissor
                 '''))-1
if choise<=2:
    computer_choise=random.randint(0,2)

    print(f'''YOUR CHOISE IS :
        {game[choise]}
        ''')

    print(f'''COMPUTER CHOISE IS :
        {game[computer_choise]}
        ''')

    result=str(choise)+str(computer_choise)

    tia=['00','11','22']
    user_win=['10','21','02']
    comp_win=['01','12','20']

    if result in tia:
        print("Game is Tia !!!")
    elif result in user_win:
        print("You win !!!")
    elif result in comp_win:
        print("You lose !!!")
else:
     print("Wrong Input Match is over \n")