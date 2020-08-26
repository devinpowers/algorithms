#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 13:13:52 2020

@author: devinpowers
"""

from time import time

start = time()
x = [i for i in range(10)]
print(x)

end = time()

elapsed = end - start

import sys
data=[]
for k in range(10):
    

    a = len(data)
    b = sys.getsizeof(data)
    print( 'Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
    
    