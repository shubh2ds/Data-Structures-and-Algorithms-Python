# [2,3,5,6,8,10] , n = 6 , sum = 10
wt  = val = arr = [2,3,7,8,10]  
n = 5
w = sum = 11
#OP: True/False # {3,8}

def knapsack(wt, val, w, n):
    if n == 0  or w == 0:
        return 0
    
    if wt[n-1] <= w:
        return max(( val[n-1] + knapsack(wt, val, w-wt[n-1], n-1) ) , knapsack(wt, val, w, n-1))
    
    elif wt[n-1] > w :
        return knapsack(wt, val, w, n-1)


output = knapsack(wt, val, w, n)
print("max profit:",output)
if output == sum:
    print(True)
else:
    print(False)