

'''Project One'''


class Person:
    '''Creates a Class of a person in our given file of names'''
    
    # Any Classes Variables Here:
        
    number_of_people_added = 0
    
    def __init__(self, first, last, email):
        
        self.first = first
        self.last = last
        self.email = email
        
        # keep track of the number of people we add 
        Person.number_of_people_added += 1
        
    def fullname(self):
        '''returns the fullname of the person'''
        return '{} {}'.format(self.first, self.last)
    
    def __repr__(self):
        return "Person('{}','{}','{}')".format(self.first, self.last, self.email)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)


    
def merge():
    pass

def merge_sort():
    pass


def order_first_name():
    pass

def order_last_name():
    pass

def is_alphabetized():
    
    '''Should rn in Big Oh (n) time and'''
    pass

def alphabetize():
    '''will return the number of comparisons made '''
    pass


