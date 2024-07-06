marks=input("Enter the all marks oof students \n").split()
high = 0
for mark in marks:
    if int(mark) > high:
        high = int(mark)
        
        
print(f"The highest score of the student is {high}")