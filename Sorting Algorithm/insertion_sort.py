


def insertion_sort(list_a):
    
    indexing_length = range(1, len(list_a))
    
    for i in indexing_length:
        
        value_to_sort =list_a[i]
        
        
        while list_a[i-1] > value_to_sort and i>0: # python allows negative indexing
            
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
        
            i = i -1
        
    return list_a


print(insertion_sort([2,12,123,122,42,312,42,124,9,10,1,2,3,45,9,0]))
        



    