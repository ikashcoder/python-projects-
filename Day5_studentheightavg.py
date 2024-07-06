
student_height =input("Enter the height of all students \n").split()

add_height=0
count=1

for height in student_height:
    
    add_height+=int(height)
    count+=1
    
avg= add_height/count

print(f"Average Height of students is {round(avg)}")