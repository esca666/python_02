class Institute:
    name = None
    address = None

    def __init__(self , name , address) :
        self.name = name 
        self.address = address

    def get_name(self):
        return self.name
    def get_address(self):
        return self.address
college = Institute('It_training ', 'putalisadak')

college.get_name()

print(college.name)
print(college.address)