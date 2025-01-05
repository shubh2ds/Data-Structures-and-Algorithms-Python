#Minimum Number of Insertion and Deletion to convert String a to String b
a = "heap"
b = "pea"

n = 4
m = 3

def LCS(a,b,n,m):
    if n == 0 or m == 0:
        return 0
    if a[n-1] == b[m-1]:
        return 1 + LCS(a,b,n-1,m-1)
    else:
        return max( LCS(a,b,n-1,m), LCS(a,b,n,m-1))
    
lcs = LCS(a,b,n,m)
print("lcs:",lcs)
insertion = m - lcs
print("insertion:",insertion)
deletion = n - lcs
print("deletion:",deletion)