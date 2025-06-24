class vehicle:
    def __init__(self,company,owner,color,current_speed):
        self.company=company
        self.owner=owner
        self.color=color
        self.current_speed=current_speed
        
    def move(self):
        print('the car has moved ')
        
    def stop(self):
        print('the car has stopped')
     
class car(vehicle):
    def display(self):
        print('this is car class')
        
    
    def move(self):
        print('that car can moved ')
        
car1=car ('toyota','bandr','black',120)

print(car1.owner)
car1.move()
