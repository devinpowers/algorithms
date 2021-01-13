
""" Hash tables """

country_code = [('25', 'USA'), ('20', 'India'), ('10', 'Nepal')]
 
def insert(item_list, key, value):
    item_list.append((key, value))
 
def search(item_list, key):
    for item in item_list:
        if item[0] == key:
            return item[1]
    
print (search(country_code, '20')) # Output: India
print (insert(country_code, '100')) # Output: None, python returns 'None' by 