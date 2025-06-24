class person:
    def __init__(self):
        self.__age= None
        
    def set_age(self,age):
        self.__age=age  
        
    
    def  get_age(self):
        return self.__age
    
p=person()
p.set_age(30)
print(p.get_age())    