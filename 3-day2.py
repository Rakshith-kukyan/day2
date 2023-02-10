''' 3. Write a Program that can print a pattern as follows
Example:
Input = 'Samarthya'
Output = ‘540S1a1m2a3r5t8h13y21a' '''
x="Python"
def fibonacci(n):
  if n<=0:
    print("Incorrect input")
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    a=0
    b=1
    fib_list=[a,b]
    for i in range(2,n):
      c=a+b
      fib_list.append(c)
      a=b
      b=c
    return fib_list
l=len(x)
a=fibonacci(l)
b=sum(a)
r=str(b)
for i in range (0,l):
    r=r+str(a[i])+x[i]
print(r)