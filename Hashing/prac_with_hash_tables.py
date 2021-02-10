#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practice

"""


##my_list = [1,2,3,4]

my_list = [x*x for x in range(4)]
mygenerator = (x*x for x in range(3))
#for i in my_list:
 #   print(i)
    
for i in mygenerator:
    print(i)
    
    
        
def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i
        
mygenerator = createGenerator()

print(mygenerator)


for i in mygenerator:
    print(i)



    

    
    
    
    
    
    
    
    
    
    
    
    