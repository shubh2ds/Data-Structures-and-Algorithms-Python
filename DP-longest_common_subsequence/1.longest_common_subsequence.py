x = "abcdgh"
n = 6
y = "abedfhr"
m = 7

#OP:"abdh" # len:4
def LCS(x,y,n,m):
    if n == 0 or m == 0:
        return 0
    if x[n-1] == y[m-1]:
        return 1 + LCS(x,y,n-1,m-1)
    else:
        return max( LCS(x,y,n,m-1) , LCS(x,y,n-1,m))
    

lcs_len = LCS(x,y,n,m)
print("lcs_len:",lcs_len)
#lcs_len: 4 : abdh
# longest common subsequence can have non continuous characters, but
# longest common substring can have only continuous characters.