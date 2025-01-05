n = 4 # size of the array
wt = [1,3,4,5] #item weights
val = [1,4,5,7]    # item price/value
w = 7 # bag capacity

#choice diagram:
# wt[n-1] <= w then item will be picked
# wt[n-1] > w  then item will not be picked, bcoz no space in bag
t = [[0]*(w+1)]*(n+1)
#t = [[0]*w for _ in range(n)]
for i in range(n+1):
    for j in range(w+1):
        t[i][j] = -1

def knapsack(wt, val, w, n):
    if n == 0  or w == 0:
        return 0
    if t[n][w] != -1:
        return t[n][w]
   
    if wt[n-1] <= w:
        t[n][w] =  max(
            ( val[n-1] + knapsack(wt, val, w-wt[n-1], n-1) ) , knapsack(wt, val, w, n-1)

        )
        return t[n][w]
    elif wt[n-1] > w :
        t[n][w] =  knapsack(wt, val, w, n-1)
        return t[n][w]

output = knapsack(wt, val, w, n)
print("max profit:",output)
#max profit: 9