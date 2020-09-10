def Partition(A ,start, end):
    
    pivot = A[end]
 
    p_index = start
    
    
    for i in range(start,end):
        print('Index:', i)
    
        if A[i] <= pivot:
            
            
            #swap number at index with the P_index!
            A[p_index], A[i] = A[i], A[p_index]
            
            p_index = p_index +1
            
        
    # this is swaping the pivot point between the sorted values
    
    A[p_index], A[end] = A[end], A[p_index]

    
    return p_index
    


         
def QuickSort(A, start, end):
    
    
    if start > end:
        return
    
    p_index = Partition(A, start, end)
    
    # recursive Calls here:
        
    QuickSort(A, start, p_index-1)
    
    QuickSort(A,p_index +1, end)
    
    

array = [7,2,1,6,8,5,3,4]

n = len(array)

QuickSort(array,0,n-1)

print(array)
    