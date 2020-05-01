#PYTHON
#4:03 12/14/2018

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + '@company.com'
        self.pay = pay 

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 5000)

#print(Employee.__dict__)
emp_1.apply_raise()
print(emp_1.pay)

emp_2.raise_amount = 1.05
emp_2.apply_raise()
print(emp_2.pay)