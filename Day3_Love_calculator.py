print('''               __,,,__
                ,-""-,-"       "-,-""-,
               /,-' , .-'-.7.-'-. , '-,\\
               \(    /  _     _  \    )/
                '-,  { (0)   (0) }  ,-'
                 /    >  .---.  <    \\
                |/ .-'   \___/   '-. \|
                {, /  ,_       _,  \ ,}
                \ {,    \     /    ,} /
                 ',\.    '---'    ./,'
             _.-""""""-._     _.-""""""-._
           .'            `._.`            '.
         _/_               _                \\
      .'`   `\            | |                \\
     /        |           | |                 ;
     |        /           |_|                 |
     \  ;'---'    _    ___  _  _  ___         ;
      '. ;       | |  /   \| || ||  _|     _ ;
        `-\      | |_ | | || |/ /|  _|   .' `,
           `\    |___|\___/ \__/ |___|  |     \\
             \            _ _           \     |
              `\         | | |         /`   _/
    ,-""-.    .'`\       | | |       /`-,-'` .-""-,
   /      `\.'    `\     \___/     /`    './`      \\
  ;  .--.   \       '\           /'       /   .--.  ;
  | (    \   |,       '\       /'        |   /    ) |
   \ ;    }             ;\   /;         `   {    ; /
    `;\   \         _.-'  \ /  `-._         /   /;`
      \ \__.'   _.-'       Y       `-._    '.__//
       '.___,.-'                       `-.,___.'
''')



def true(name1):
    T=name1.count('t')
    R=name1.count('r')
    U=name1.count('u') 
    E=name1.count('e') 
    
    result=T+R+U+E
    return result

def love(name2):
    
    L =name2.count('l')
    O =name2.count('o')
    V =name2.count('v')
    E =name2.count('e')
    
    result =L+O+V+E
    return result

print('''•´¯`•.   🎀  *** 𝒯𝒽𝒾𝓈 𝒾𝓈 𝐿🏵𝓋𝑒 𝒞𝒶𝓁𝒸𝓊𝓁𝒶𝓉🏵𝓇 ***  🎀   .•`¯´•''')

you=(input("𝗘𝗻𝘁𝗲𝗿 𝗬𝗼𝘂𝗿 𝗡𝗮𝗺𝗲 :\n")).lower()
your_partner =(input("𝗘𝗻𝘁𝗲𝗿 𝗛𝗲𝗿 𝗡𝗮𝗺𝗲 :\n")).lower()

for_true=str(true(you)+true(your_partner))
for_love=str(love(you)+love(your_partner))

score =int(for_true+for_love)

#print(score)

if score<=10 or score>=90:
    print(f'''Your Love Score is :{score} ;••÷  🎀  𝒴💮𝓊 𝑔😍 𝓉💙𝑔𝑒𝓉𝒽𝑒𝓇 𝓁𝒾𝓀𝑒 𝒸❤𝓀𝑒 𝒶𝓃𝒹 𝓂𝑒𝓃𝓉❤𝓈 ❢❣❢  🎀  ÷••''')
    
elif score>=40 or score<=50:
    print(f"Your Love Score is :{score} ; 𝗬𝗼𝘂 𝗮𝗿𝗲 𝗯𝗼𝘁𝗵 𝗮𝗹𝗿𝗶𝗴𝗵𝘁 𝘁𝗼𝗴𝗲𝘁𝗵𝗲𝗿 !!!")
    
else:
    print(f"Your Love Score is :{score} \n")