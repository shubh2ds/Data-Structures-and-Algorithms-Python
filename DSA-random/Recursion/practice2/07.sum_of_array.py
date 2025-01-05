def sum_of_array(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    
    return arr[0] +sum_of_array(arr[1:])

print(sum_of_array([11,2,3,4]))
