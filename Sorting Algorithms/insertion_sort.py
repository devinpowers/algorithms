

''' insertion sort Algorithm'''



def insertion_sort(list_to_sort):
    
    indexing_length = range(1, len(list_to_sort))
        
    for i in indexing_length:
        
        value_to_sort = list_to_sort[i]
        
        
        while list_to_sort[i-1] > value_to_sort and i>0: # python allows negative indexing
            
            list_to_sort[i], list_to_sort[i-1] = list_to_sort[i-1], list_to_sort[i]
        
            i = i -1  # move down the sorted list to check if number is less than the previous number
        
    return list_to_sort



print(insertion_sort([2,12,1,0,42,312,42,124,9,10,1,2,3,45,9,0]))
        

'''output'''

[0, 0, 1, 1, 2, 2, 3, 9, 9, 10, 12, 42, 42, 45, 124, 312]



'''More Practice with sort algorithm'''


def insertion_sort_alg(unsorted_list):
    
    
    iterations_of_list = range(1, len(unsorted_list))  # number of times we need to check the list of numbers, since we need to check every number/ index
    
    for i in iterations_of_list:
        
        item_to_be_sorted = unsorted_list[i]
        
        while item_to_be_sorted < unsorted_list[i-1] and i > 0:
            
            unsorted_list[i], unsorted_list[i-1] = unsorted_list[i-1], unsorted_list[i]
            
            i = i -1
            
    
    return unsorted_list
            
            
            

    


print(insertion_sort_alg([2,3,8,10,0,6,8,9,10,12,200,200,250,300,2,1,25,0,69,20]))