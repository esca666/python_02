# class and object - Inheritance

class vehicle:
    name = 'vehicle name'
    def get_name(self):
        return self.name 
    wheel = 1

class bikes(vehicle):
    vehicle_type = None

   
class car(vehicle):
    vehicle_type = None

    @staticmethod   #it is also known as decorator... yesley chai function lai chai as a argument pathauxa
    
    def check_car_wheel():
        pass


    def get_vehicle_type(self):
        self.check_car_wheel()
        return self.vehicle_type
    
c1 =car()
b1 = bikes()
print(b1.wheel)
print(c1.wheel)
print(c1.get_vehicle_type())
print(b1.get_name())

