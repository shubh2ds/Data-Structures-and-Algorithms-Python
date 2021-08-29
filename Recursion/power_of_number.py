## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)
## a, b = input().split()
## a = int(a)
## b = int(b)
#2^3=2*2*2= 2^1 ie x and *2^2 ie x^n-1
def power_of_num(x,n):
  if n==0:
    return 1
  if n==1:
    return x

  return x * power_of_num(x,n-1)

x,n=input().split()
x=int(x)
n=int(n)
print(power_of_num(x,n))
