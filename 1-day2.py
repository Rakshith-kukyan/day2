'''1. Given a number N, find sum of all GCDs that can be formed by selecting all the pairs
from 1 to N.'''
import math
sum=0
n=int(input("Enter the number: "))
for i in range (1,n+1):
    for j in range(i+1,n+1):
        a=math.gcd(i,j)
        sum+=a
print(f"The sum gcd's is: {sum}")