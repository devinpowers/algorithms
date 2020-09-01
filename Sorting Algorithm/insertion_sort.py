

''' insertion sort Algorithm'''



def insertion_sort(list_to_sort):
    
    indexing_length = range(1, len(list_to_sort))
    
    for i in indexing_length:
        
        value_to_sort =list_to_sort[i]
        
        
        while list_to_sort[i-1] > value_to_sort and i>0: # python allows negative indexing
            
            list_to_sort[i], list_to_sort[i-1] = list_to_sort[i-1], list_to_sort[i]
        
            i = i -1
        
    return list_to_sort



print(insertion_sort([2,12,123,122,42,312,42,124,9,10,1,2,3,45,9,0]))
        



[0, 1, 2, 2, 3, 9, 9, 10, 12, 42, 42, 45, 122, 123, 124, 312]

