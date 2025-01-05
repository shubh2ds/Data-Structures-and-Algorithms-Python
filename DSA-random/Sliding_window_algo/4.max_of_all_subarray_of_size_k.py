arr = [2,5,1,8,2,9,1]
size = 7
k = 3
i = j = 0
results = []
maxm = 0
while j<len(arr):
    #if arr[j]>max:
    #    max= arr[j]
    if j-i+1< k:
        j=j+1
    elif j-i+1 == k :
        results.append(max(arr[i:j+1]))

        i = i+1
        j = j+1

print(results)