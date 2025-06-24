book_number={'1111':{'amal'},
             '2222':{'mha'},
             '3333':{'bader'},
             '4444':{'jabeer'}
             }

enter=input('Please chose the process. create, read name, read number, update, or delete?')

     
     


def create_itmes(number,name):

     if len(number)!=4 or not name.isalpha():
          print("invalid")

     else:
         
          book_number[number]=name
          print(book_number)

def read(number):
     if (number not in book_number): #[number])
          print("Nmber not found in phone book ")
     else:
      print(book_number[number]) 
 
def delete(number):
     if (number not in book_number):
          print('Nmber not found in phone book')
     


     else:
          book_number.pop(number)
          print(book_number)

     
def update(num, name):
    if len(num) != 4 or not num.isdigit():
        print("❌ Invalid number: It must be exactly 4 digits.")
        return
    elif num not in book_number:
        print('number is invalid')
        return
    elif not name.isalpha():
        print("❌ Invalid name: It must contain only letters.")
        return
    else:
        book_number[num] = {name}
        print("Updated dictionary:")
        print(book_number)
    
if(enter=='create'):
     input_num=input('enter number')
     input_name=input('enter name')
     create_itmes(input_num,input_name)
    

elif(enter=='read'):
    input_num=input('enter number')
    read(input_num)

elif(enter=='delete'):
     input_num=input('enter items for delete')
     delete(input_num)
     # print(book_number)

elif(enter=='update'):
    input_num=input('enter number for update')
    enter_name=input('enter name you want save')
    update(input_num, enter_name)
    print(book_number)



