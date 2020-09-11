

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

    def __eq__(self, o):
        return self.first == o.first and self.last == o.last and self.email == o.email
    
    
def Merge(Left, Right, Array):
    
    '''Merges left and right sides of an array'''
    
    Left_length = len(Left)
        
    Right_length = len(Right)
    
    i = j = k = 0
        
    while (i < Left_length and j < Right_length):
        
        if Left[i] <= Right[j]:
            Array[k] = Left[i]
            i = i + 1
        
        else:
            Array[k] = Right[j]  
            j = j+ 1
        k = k + 1
        
    # in case one of the letters runs out before the other
    while i < Left_length:
        
        Array[k] = Left[i]
        i = i + 1
        k = k + 1
        
    while j < Right_length:
        
        Array[k] = Right[j]
        j = j + 1
        k = k + 1
        
    return Array




def Merge_Sort(Array): 
    '''Recursive function to sort an Array'''
    n = len(Array)
    
    if n < 2:    
        return
    middle = n // 2
    
        # have to make right and left subarrays        
    Left = Array[0:middle]
          
    Right = Array[middle:]
  
        #Recursive functions

    Merge_Sort(Left)
    
    Merge_Sort(Right)
      
    # calling the merge function
    Merge(Left, Right, Array)




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


