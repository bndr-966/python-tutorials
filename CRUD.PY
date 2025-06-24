phoneNumber={
    "1111111111":{"amal"},
    "2222222222":{"Mohamd"},
    "3333333333":{"Noa"},
    "4444444444":{"Robee"},
    "5555555555":{'malk'}
}
enter=input('Please chose the process. create, read name, read number, update, or delete?')

#function definetion


def create_contact(contactNumber, contactName):         #create_contact
    phoneNumber[contactNumber]= contactName

# output for Name 
def read_name(number):
    print(phoneNumber[number])

# output for Name
# def read_number(name): #not right             
#     print(phoneNumber[name])


# output for delete
def delete_by_name(number):
    phoneNumber.pop("number")
    print(phoneNumber)
#phoneNumber.pop(key)
def delete_by_number(name):

    phoneNumber.pop(name)
    print(phoneNumber)
# output for updatedelete

def update_name(number):
    phoneNumber ['number']
    print(phoneNumber)

def update_number(name):
    phoneNumber ['name']
    print(phoneNumber)
    

# key = input("Enter the key you want to update: ")

#functions calling
if(enter=="create"):
    input_number=input('please enter the number')
    input_name=input('please enter the name')
    create_contact(input_number, input_name)
    


elif(enter=="read number"):
    input_name=input('please write the Name you are looking for')
    read_number(input_name)

elif(enter=="read name"):
    input_number=input("please write the number you are looking for")
    read_name(input_number)

elif(enter=="delete"):
    
    input_name = input("Please Enter the number you want to delete")
    delete_by_number(input_name)
    print(phoneNumber)


elif(enter=="update"):
     input_number=input("please write the number you are update for")
     update_name=input('please write the name you are update for')
    #  phoneNumber[ input_name ]= update_name
     phoneNumber.update({input_number: update_name})

     print(phoneNumber)

#     update_number()

else: 
    print("invalid input")


