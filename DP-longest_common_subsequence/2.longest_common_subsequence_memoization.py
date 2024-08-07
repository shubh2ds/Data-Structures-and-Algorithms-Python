x = "abcdgh"
n = 6
y = "abedfhr"
m = 7

t = [[-1]*(m+1)]*(n+1)
print(t)
# for i in range(0 , n+1):
#     for j in range(0 , m+1):
#         t[i][j] = -1
#OP:"abdh" # len:4
def LCS(x,y,n,m):
    if n == 0 or m == 0:
        return 0
    if t[n][m] != -1:
        return t[n][m]
    
    if x[n-1] == y[m-1]:
        t[n][m] =  1 + LCS(x,y,n-1,m-1)
        return t[n][m]
    else:
        t[n][m] =  max( LCS(x,y,n,m-1) , LCS(x,y,n-1,m))
        return t[n][m]

lcs_len = LCS(x,y,n,m)
print("lcs_len:",lcs_len)
#lcs_len: 4 : abdh
# longest common subsequence can have non continuous characters, but
# longest common substring can have only continuous characters.