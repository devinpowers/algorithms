#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practice

"""

size = 10

key = "jill"

# hash sum will be an index for our internal buckets array!

hash_sum = 0

for index, c in enumerate(key):
    ##print(index, ": ", c)
    
  ## print("Index  + length of key: ", index, ": ", len(key), " c is: ", c, " what is order for this c?: ", ord(c))
    
    
    hash_sum  += (index + len(key)) ** ord(c)
    
    hash_sum = hash_sum % size


print("Hash Sum Return for", key, "is: ", hash_sum)



    

    
    
    
    
    
    
    
    
    
    
    
    