'''4. Write a Program to remove all the duplicate characters from a string
Example:
Input = 'Ssaamarrthyya'
Output = 'ahmrsty' '''
x="Baggage"
c = ""
for char in x:
    if char not in c:
        c=c+char
a=c.lower()
b=sorted(a)
r=""
for i in range(0,len(b)):
    r=r+b[i]
print(f"Sorted string with no duplicates is: {r} ")