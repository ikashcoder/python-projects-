
def Days_in_yearMonth(year,month):
    
    if year%4==0:
        if year%100!=0:
                condition=True 
        else :
            if year%400==0:
                condition=True          
            else:
                condition=False
                
    else:
                condition=False
                
    if condition==True:
        Month_Days=[31,28,31,30,31,30,31,31,30,31,30,31]
        Days =Month_Days[month-1] 
        return Days
    else:
        Month_Days=[31,29,31,30,31,30,31,31,30,31,30,31]
        Days =Month_Days[month-1] 
        return Days

condition=False
stop =False

while not stop:
    print("This is Days shower tool in particular year and month \n !!!")
    year=int(input("Enter year \n"))
    month =int(input("Enter Month\n"))
    
    Day=Days_in_yearMonth(year,month)
    
    print(f"{year} : {month} : and {Day} in {month} that month \n")
    
    
    
    


