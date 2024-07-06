Box1=["⬜️","⬜️","⬜️"]
Box2=["⬜️","⬜️","⬜️"]
Box3=["⬜️","⬜️","⬜️"]
map=[Box1,Box2,Box3]

print(f"{Box1}\n{Box2}\n{Box3}")

print("@ 𝔗𝔥𝔞𝔱 𝔦𝔰 𝔪𝔞𝔭 𝔱𝔬 𝔰𝔱𝔬𝔯𝔢 𝔱𝔥𝔢 𝔗𝔯𝔢𝔞𝔰𝔲𝔯𝔢 @")
position=input('''Enter the position Where you want to store your Treasure ....
    1st number should be the row or horizontal line 
    2nd number shhould be the column or vertical line 
    ''')

row=int(position[0])
column =int(position[1])



map[row-1][column-1]="🚩"

print(f"{Box1}\n{Box2}\n{Box3}")

