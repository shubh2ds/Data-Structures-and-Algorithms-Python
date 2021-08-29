def fibonacci(n):
  if n==1 or n==2:
    return 1
  return fibonacci(n-1)+fibonacci(n-2)
n=3  #0,1,1,2,3,5,..

fibonacci(n)
