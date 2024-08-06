arr = [12,-1,-7,8,-16,30,16,28]
# op:[-1, -1, -7, -7, -16, -16]
size = 8
k = 3

i = j = 0
results = []
tmp= []
while j<len(arr):

    if arr[j]<0:
        tmp.append(arr[j])
    
    if j-i+1 < k:
        j = j+1
    elif j-i+1 == k:
        if tmp != []:
            results.append(tmp[0])

            #tmp.remove(tmp[0])
            
        i = i+1
        j = j+1
        if arr[i]<0:
            tmp.insert(0,arr[i])
print(results)

