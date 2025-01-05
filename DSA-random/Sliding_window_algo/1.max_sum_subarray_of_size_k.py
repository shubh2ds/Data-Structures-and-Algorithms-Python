arr = [2,5,1,8,2,9,1]
size = 7
k = 3

i = j = sum = 0
max = 0
while j<len(arr):
    sum = sum+arr[j]
    if j-i+1 < k:
        j = j + 1
    elif j-i+1 == k:
        if sum>max:
            max = sum
        sum = sum - arr[i]
        j = j+1
        i = i+1

print(max)