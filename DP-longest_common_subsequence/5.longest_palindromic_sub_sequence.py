a = "agbcba"
b = a[::-1]

n = 6
m = 6

def LCS(a,b,n,m):
    if n == 0 or m == 0:
        return 0
    if a[n-1] == b[m-1]:
        return 1 + LCS(a,b,n-1,m-1)
    else:
        return max( LCS(a,b,n-1,m), LCS(a,b,n,m-1))
    
lps = LCS(a,a[::-1],n,m)
#LPS = LCS(a,reverse(a))
print("lps:",lps)
#OP:5