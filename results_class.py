class result: #here class_name is local to its own function

    def __init__(self,class_name): 
        self.class_name = class_name

    @staticmethod
    def get_student_count(class_name):
        if class_name==1:
            return 100
        elif class_name==10:
            return 40
        else:
            raise ValueError(f'I dont have that data.{class_name}')
    @staticmethod
    def get_student_count(class_name):
      
        if class_name==2:
            return 90
        elif class_name==10:
            return 40
        else:
            raise ValueError(f'I dont have that data.{class_name}')
        
 


    def get_total_student(self):
        student_count = self.get_student_count(self.class_name)
        return student_count
    
result_1 =result(2)
print(result_1.get_total_student())