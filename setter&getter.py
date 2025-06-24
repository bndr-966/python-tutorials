# class bank:
#     def set_name(self,name):
#         if (type(name)==int):
#             self.name=name
#         else:
#             print('the value is not integer')
        
#     def get_name(self):
#         return self.name
    
#     def increment_name(self):
#         self.name+=1

        
    
# b=bank()
# b.name=10
# b.__increment_name()
# print(b.get_name)
# b.set_name(10)
# print(b.get_name()) 
#    ////////////////////////////////
class funcation:
    def set_val(self,val):
        if(type(val==int)):
            self.val=val
        else:
            print('the value is not integer')
            
    def get_val(self):
        return self.val
    
    def __increment_val(self):
        self.val*=5
    
    def get_increment(self):
        self.__increment_val()
        return self.val
        
        
    
        
n=funcation()

n.val=10 
# n.set_val(11) 
print(n.get_increment())
        