def power_of_n(x,n):
    if n==0:
        return 1
    if n ==1:
        return x
    return x**power_of_n(x,n-1)
    # 2^0 , 2^1, 2^2 = 2*2, 2^3 = 2*2*2
print(power_of_n(2,3))