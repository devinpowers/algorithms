
class Employee:
    
    #class variable
    
    raise_amount = 1.04
    
    def __init__(self, first, last, email, pay):
    
        
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay
        
    def fullname(self):
        
        '''returns the fullname of the person'''
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        
        self.pay = int(self.pay * self.raise_amount)
    
    
    
    
emp_1 = Employee('Devin','Powers', 'powers88@msu.edu', 50000)

emp_2 = Employee('Lebron', 'James', 'LBJ@lakers.com', 60000)


#print(Employee.raise_amount)

emp_1.raise_amount = 1.05
print(Employee.raise_amount)
print(emp_1.raise_amount)

print(emp_2.raise_amount)

print(emp_1.__dict__)
print(emp_2.__dict__)