# كود برمجي خاص بالكلاس 

# class Student:      
#     def __init__(self,name,age,id,grades):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.grades=grades
#     def talk(self):
#         print('my Name is',self.name ,'I am',self.age ,'years old')
#         # print('I am',self.age ,'years old')

# stud1=Student ('Bandr',24,'0500',100)
# # print(stud1.name)
# # stud1.talk()
    # /////////////////////////////////

# class student:
#     def talk(self):
#         print(self)
# std1=student()
# std2=student()

# std1.talk()
# std2.talk()
#/////////////////////////////////////  
class Bicycle:
    def __init__(self, description, cost, sale_price, condition):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self._sold = False  # Encapsulated attribute 
    def update_sale_price(self, new_price):
       
        if self._sold:
            print('Action not allowed, Bike has already been sold') 
        else:
            self.sale_price = new_price
    

    def sell(self): 
        self._sold = True
        print('Action not allowed, Bike has already been sold')
                                                    

    def is_sold(self):
        return self._sold

    def display_info(self):
        print('Description:', self.description)
        print('Cost:', self.cost)
        print('Sale Price:', self.sale_price)
        print('Condition:', self.condition)
        print('Sold:', self._sold)

# Example usage
bike1 = Bicycle('Univega Alpina, orange', cost=100, sale_price=500, condition='Used')
#bike1.update_sale_price(350)
# bike1.sell()
bike1.is_sold()
k=int(input("please enter new price value"))
bike1.update_sale_price(k)  # Should be blocked
bike1.display_info()

# bike1.v_hour=22
# print(dir(bike1))
# del bike1.v_hour
# print(dir(bike1))

        
# print(bike1.university_name)
          
# class book_student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
#     def read(self):
#         print('my name: ',self.name)
#         print('my id: ',self.id)
#         print('my age: ',self.age)

# std1=book_student("bandr","050x0",24)
# std2=book_student('mlak','050z0',28)
# std1.read()