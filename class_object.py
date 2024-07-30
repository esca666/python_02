#class and object

class Electronic:
    operating_system = 'window'
    ram = None
    hard_disk = None
    cpu = None
    def __init__(self,ram,hard_disk,cpu):
        self.ram = ram
        self.hard_disk=hard_disk
        self.cpu=cpu
        


    def get_ram(self):
        return self.ram
    
laptop = Electronic(4,500,2.70)
laptop.get_ram()

print(laptop.ram)
print(laptop.hard_disk)
print(laptop.operating_system)
print(laptop.cpu)


