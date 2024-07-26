def merge_sorted(a1,a2,arr):
    i=0
    j=0
    k=0
    while i<len(a1) and j<len(a2):
        if a1[i]<=a2[j]:
            arr[k]=a1[i]
            i=i+1
            k=k+1
        else:
            arr[k]=a2[j]
            j=j+1
            k=k+1
    while i<len(a1):
        arr[k]=a1[i]
        i=i+1
        k=k+1
    while j<len(a2):
        arr[k]=a2[j]
        j=j+1
        k=k+1
    
a1=[1,2,3,4,7,9]
a2=[2,3,5]
a=[1,2,3,4,7,9,2,3,5]
merge_sorted(a1,a2,a)
