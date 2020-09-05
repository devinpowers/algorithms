

''' QuickSort '''



def Partition(A, Start, End):
    '''Selecting the Pivot and Stuff'''
    
    Pivot = A[End]
    
    p_index = A[Start-1]
    
    for i in range(Start, End):
        if A[i] <= Pivot:
            A[i] = A[p_index]
        
        p_index = p_index +1
    
    A[p_index] = A[End]
    
    return p_index

    
    
    



def QuickSort(Array, Start, End):
    
    if Start >= End:           # exit condtions
        return
    
    p_index = Partition(Array,Start,End)
    
    
    QuickSort(Array, Start, p_index -1)
    
    QuickSort(Array, p_index+1, End)


a = [3,4,2,31,223,12,0,40]

n = len(a)

QuickSort(a,0, n-1)


    