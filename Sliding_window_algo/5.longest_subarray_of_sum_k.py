arr = [4,1,1,1,2,3,5]
i=j=0
k = 5
longest = 0
summ = 0
while j<len(arr):

    summ = summ + arr[j]
    if summ < k:
        j = j+1
    elif summ == k :
        longest = max(j-i+1, longest)
        summ = summ - arr[i]
        i = i + 1
        j = j + 1
    elif summ > k:
        while summ>k:
            summ = summ - arr[i]
            i = i + 1

        summ = summ - arr[j]
print(longest)


