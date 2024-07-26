def get_sum(n):
    if n==0:
        return 0
    return n+get_sum(n-1)

print(get_sum(4))