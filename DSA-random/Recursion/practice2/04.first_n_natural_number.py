def n_1_natural(n):
    if n<=0:
        return 
    print(n)
    return n_1_natural(n-1)

def _1_n_natural(n):
    if n<=0:
        return 
    _1_n_natural(n-1)
    print(n)
    return 

_1_n_natural(5)