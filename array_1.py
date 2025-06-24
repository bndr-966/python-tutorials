# # num =int(input('enter number: '))
# # sum_of_numbers = 0
# # while(num > 0):
# #     sum_of_numbers += num
# #     num -= 1
# # print("The sum is", sum_of_numbers) 

# n=15
# sum=0
# while (n>0):
#  sum+=n
#  n-=1
# print("the sum is:" , sum)


# # Write a program that prints the numbers from 1 to 10 using a for loop.

#         # for w in range(1,11):
#         #     print(w)

# #  even number
# b=1
# e=21
# for x in range(b, e):
#     if x %2 ==0 :
#         print(x)
# # secretNumber=7      
# # guess= int(input(f'Take a guess of the secret number '))
# # print(guess)
# # while True:
# #     print("Please guess a number between 1 & 10")
# #     if guess==secretNumber:
# #         print ("you win")
# #         break
# #     elif guess>secretNumber :
# #         print("The secret number is smaller, please try again")
# #     # elif guess<secretNumber :
# #         # print("The secret number is bigger, please try again")   
    
# my_age=input("enter your age:") 
# print("you are", my_age, "years old!")
# my_name,add= "bandr" ,25 
# print("my name:",my_name,  "    " ,"my age:",add )

# my_list=("bandr", "farj" ,"saeed", "malk")
# # my_list.append("hamad")
# print(type(my_list))
# print(my_list)

# # m=0
# # a=10
# # for (10>m) :
# #     m+=1
# # print(m)

# g=19
# while g>=-3:
#     print(g)
#     g-=1

start_value = 10  # You can change this to any starting number

for i in range(start_value, -1):
    #this line prints i varaible
    print(i)
student=1
sum=0
while student<=6:
    grade=int(input( "enter grade :"))
    
    student+=1
    sum=sum + grade

print(sum/6)