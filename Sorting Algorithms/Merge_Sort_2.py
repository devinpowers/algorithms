


def Merge (Left, Right, Array):
    
    Left_length = len(Left)
    
    Right_length = len(Right)
    
    i = j = k = 0
    
    while (i < Left_length and j < Right_length):
        
        if Left_length[i] <= Right_length[j]:
            
            Array[k] = Left_length[i]
            i = i + 1
        
        else:
            Array[k] = Right_length[j]
            j = j+ 1
            
        
        k = k + 1
    
    # in case one of the letters runs out before the other
    while i < Left_length:
        
        Array[k] = Left_length[i]
        i = i + 1
        k = k + 1
        
    while j < Right_length:
        
        Array[k] = Right_length[j]
        j = j + 1
        k = k + 1
        
    return Array



def Merge_Sort(Array):
    '''Recursive function to sort an Array'''
    
    n = len(Array)
    
    if n < 2:

        return
    
    mid = n // 2
    
    Left = n[:mid]
    
    Right = n[mid::]
    
    
    for i in range(Left):
        
        Left[i] = A[i]
        
    for i in range(Right):
        
        Right[i-mid] = A[i]
        
    Merge_Sort(Left)
    
    Merge_Sort(Right)


    Merge(Left, Right, Array)    
    
    
n = [2,4,1,6,8,5,3,7]

print(Merge_Sort(n))
    