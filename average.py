# student=1
# sum=0
# while student<=6:
#     grade=int(input( "enter grade :"))
    
#     student+=1
#     sum=sum + grade
          
#             ##             

# print(sum/6)

student = 1
total = 0

while student <= 6:
    grade = int(input("Enter grade: "))  # Convert input to integer
    total += grade
    student += 1

average = total / 6
print("Average grade:", average)