#longest common substring
x = "abcde"
n = 5
y = "abfce"
m = 5
longest = 0
#OP:"abdh" # len:4
def LCS(x,y,n,m):
    global longest
    if n == 0 or m == 0:
        return 0
    if x[n-1] == y[m-1]:
        longest = max(longest, 1 + LCS(x,y,n-1,m-1) )
        return 1 + LCS(x,y,n-1,m-1)
    else:
        LCS(x,y,n,m-1)
        LCS(x,y,n-1,m)
        
        return 0 
    

lcs_len = LCS(x,y,n,m)
print("longest:",longest)
#lcs_len: 2 : ab
# longest common subsequence can have non continuous characters, but
# longest common substring can have only continuous characters.