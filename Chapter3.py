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
    
    
import ctypes # provides low-level arrays 

class DynamicArray:
    
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
    
    def __len__(self):
        
        return self._n
    
    def __getitem__(self,k):
        
        if not 0 <=k < self._n:
            raise IndexError('Invalid index')
        
        return self._A[k]
    
    def append(self,obj):
        
        if self._n == self._capacity:
            self._resize(2*self._capacity)
            self._A[self._n] = obj
            self._n += 1
    
    def  _resize(self, c):
        
        '''”Resize internal array to capacity c.””'''
        B = self._make_array(c)
        
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c
    
    def _make_array(self,c):
        
        return(c*ctypes.py_object)()
        
        
devin = DynamicArray()

devin._make_array(12)


# Python list class

from time import time
def compute_average(n):
    data =[]
    start = time()
    for k in range(n):
        data.append(None)
    
    end = time()
    return (end-start)/ n


































        
    
