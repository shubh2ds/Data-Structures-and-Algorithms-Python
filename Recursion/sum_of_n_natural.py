def summ_n_natural(n):
  if n==1:
    return n
  summ=n
  return summ+summ_n_natural(n-1)
n=4
summ_n_natural(n)
