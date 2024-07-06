student ={
    "Ram" :98,
    "Manoj":67,
    "Rahul":45,
    "Santosh":66,
    "Akash":100 ,
    "Sanket":75
}

for key in student:
    
    mark = student[key]
    
    if mark <=100 and mark >=91:
        print(f"{key} your Grade is Exellent and you got {mark} marks !!! congratulation ** \n")
    elif mark <=90 and mark >=81:
        print(f"{key} your Grade is best and you got {mark} marks !!! congratulation ** \n")
    elif mark <=80 and mark >=71:
        print(f"{key} your Grade is Good and you got {mark} marks !!! congratulation **\n")
    elif mark <=70 and mark >=61:
        print(f"{key} your Grade is Fail and you got {mark} marks !!! Sorry for you **\n")
    else:
        print(f"{key} your Grade is Fail and you got {mark} marks !!! Sorry for you **\n")
    
    
        
    