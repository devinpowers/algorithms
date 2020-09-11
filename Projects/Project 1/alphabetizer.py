

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
    
    
def merge(left, right, ordering):
    
    """
    Merges two lists in alphabetical order
    :param a: a list of People
    :param b: a list of People
    :param c: a function that orders two People
    :return: a merged list of param a and b, and a count of the comparisons
    """
    merged = []
    count = 0
    while left and right:
        #count of number of comparisons made
        count += 1
        #Get the correct name from either side
        if ordering(left[0], right[0]):
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    #Add remaining names to the merged list
    if left:
        merged += left
    if right:
        merged += right
    #the merged list and count
    return merged, count

def merge_sort(roster, ordering):
    """
    Sorts roster using the ordering function and merge sort
    :param a: a list of People
    :param b: a function that orders two people
    :return: a sorted version of roster
    """
    count = 0
    
    #already sorted if only one item
    if len(roster) <= 1:
        return roster, count
    
    #Sort left and right sides
    
    left, l_count = merge_sort(roster[len(roster)//2:], ordering)
    
    right, r_count = merge_sort(roster[:len(roster)//2], ordering)
    
    #Merge the lists
    
    merged_list, m_count = merge(left, right, ordering)
    
    #Add the counts
    
    count += l_count + r_count + m_count
    
    #the merged list and count
    return merged_list, count




def order_first_name(a, b):
    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    if (a.first < b.first) or (a.first == b.first and a.last < b.last):
        return True
    return False


def order_last_name(a, b):
    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    if (a.last < b.last) or (a.last == b.last and a.first < b.first):
        return True
    return False



def is_alphabetized():
    
    '''Should rn in Big Oh (n) time and'''
    pass

def alphabetize(roster, ordering):
    
    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a sorted version of roster
    :return: the number of comparisons made
    """
    
    roster, count = merge_sort(roster, ordering)
    
    return (list(roster), count)


