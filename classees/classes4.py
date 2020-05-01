#PYTHON

class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + '@company.com'
        self.pay = pay 

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('>>', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 5000, 'Python')
dev_2 = Developer('Test', 'User', 6000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])

#print(mgr_1.email)

mgr_1.print_emps()

#print(dev_1.prog_lang)
#print(dev_2.email)

S = {['him', 'sell'], [90, 28, 43]}

print([0][1][1])