class EMP:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
        print("ID= {}\nName= {}\nsalary= {}".format(self.id,self.name,self.salary))
