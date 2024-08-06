n = 4 # size of the array
wt = [1,3,4,5] #item weights
val = [1,4,5,7]    # item price/value
w = 7 # bag capacity

#choice diagram:
#
def knapsack(wt, val, w, n):
    if n == 0  or w == 0:
        return 0
    else:
        if wt[n-1] <= w:
            return max(
                ( val[n-1] + knapsack(wt, val, w-wt[n-1], n-1) ) , knapsack(wt, val, w, n-1)

            )
        elif wt[n-1] > w :
            return knapsack(wt, val, w, n-1)


output = knapsack(wt, val, w, n)
print("max profit:",output)
#max profit: 9