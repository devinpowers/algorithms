#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 14:29:10 2020

@author: devinpowers
"""



def merge(S1, S2, S):
  """Merge two sorted Python lists S1 and S2 into properly sized list S."""
  i = j = 0
  while i + j < len(S):
    if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
      S[i+j] = S1[i]      # copy ith element of S1 as next item of S
      i += 1
    else:
      S[i+j] = S2[j]      # copy jth element of S2 as next item of S
      j += 1

def merge_sort(S):
  """Sort the elements of Python list S using the merge-sort algorithm."""
  n = len(S)
  if n < 2:
    return                # list is already sorted
  # divide
  mid = n // 2
  S1 = S[0:mid]           # copy of first half
  S2 = S[mid:n]           # copy of second half
  # conquer (with recursion)
  merge_sort(S1)          # sort copy of first half
  merge_sort(S2)          # sort copy of second half
  # merge results
  merge(S1, S2, S)        # merge sorted halves back into S


S = [85,24,63,45,17,31,96,50]

merge_sort(S)

print(S)

'''Returned'''


def msort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = msort(x[:mid])
    z = msort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result



f = [2,31,31,4,231,231,4,20,23,0]
print(msort(f))

'''https://www.edureka.co/blog/python-program-merge-sort/#:~:text=Advantages%20and%20Usage-,What%20is%20Merge%20Sort%20in%20Python%3F,for%20merging%20the%20sorted%20arrays.'''
def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
 
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0      
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1
 
        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1
 
        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)
 
nlist = [3,1,4,1,5,9,2,6,5,4]
mergeSort(nlist)
print(nlist)


