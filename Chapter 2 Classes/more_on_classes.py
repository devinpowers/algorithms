

class Customer:
    
    ''' Customer Class'''
    '''Creating Objects as Customers '''
    
    '''constructor'''
    
    def __init__(self, name, membership_type):
        
        self.name = name
        self.membership_type = membership_type
    
    
        


customer = [Customer("Devin", "Gold"),
           Customer("Brad", "Bronze")
           ]

print(customer[1].name)