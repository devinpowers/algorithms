
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 



''' QuickSort '''



def Partition(A, Start, End):
    
    '''Selecting the Pivot and Stuff'''
    
    i = (Start -1)
    
    Pivot = A[End]
    

    
    for j in range(Start, End):
        
       
        if A[j] <= Pivot:
            i = i +1
            
            A[i], A[j] = A[j], A[i]
    
    
    A[i+1], A[End] = A[End], A[i+1]
    
    p_index = i 
    
    return (p_index +1)


def QuickSort(Array, Start, End):
    
    if Start >= End:           # exit condtions
        return
    
    p_index = Partition(Array,Start,End)
    
    QuickSort(Array, Start, p_index -1)
    
    QuickSort(Array, p_index+1, End)
    
    
    


a = [3,4,2,31,223,12,0,40]

n = len(a)

print(QuickSort(a,0, n-1))



    