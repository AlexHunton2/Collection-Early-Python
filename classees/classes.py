# PYTHON 
#LEARNED BY ALEX HUNTON AT 12/14/2018 3:40
#TAUGHT BY https://www.youtube.com/watch?v=ZDa-Z5JzLYM

class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last + '@company.com' 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Corey', 'Schafer')
emp_2 = Employee('Test', 'User')

#print(emp_1)
#print(emp_2)
print(emp_1.email)
print(emp_1.fullname())

#OUTPUT: CoreySchafer@company.com Corey Schafer