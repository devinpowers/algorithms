

class Customer:
    
    ''' Customer Class'''
    '''Creating Objects as Customers '''
    
    '''constructor'''
    
    def __init__(self, name, membership_type):
        
        self.name = name
        self.membership_type = membership_type
        
    
    def update_membership(self, new_membership):
        print('Calculating Costs')
        self.membership_type = new_membership
    
    @property
    def name(self):
        print("getting name")
        return self._name
    
    @name.setter 
    def name(self, name):
        print("setting name")
        self._name = name
   

    def __str__(self):
        return self.name + " " + self.membership_type
        
    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
       
        '''Comparison'''
        
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False
    
    __repr__ = __str__
     
    
    
        
customers = [Customer("Devin", "Gold"), Customer("Caleb", "Silver")]

print(customers[0].name)
