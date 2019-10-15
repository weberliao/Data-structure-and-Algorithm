def quicksort(a):
    left = []
    right = []
    middle = []
    
    if len(a)>1:
        
        pivot = a[0]
        for i in a:
            if i < pivot:
                left.append(i)
            elif i == pivot:
                middle.append(i)
            else:
                right.append(i)
    else:
        return a

    return quicksort(left) + middle + quicksort(right)
