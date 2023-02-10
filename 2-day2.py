'''2. Write a Program that can print a pattern as follows
Example:
Input1 = 'Samarthya'
Input2 = 'Club'
Output = 'SCalmuabrthya' '''
ip1="Python"
ip2="Bootcamp"
r=""
if len(ip1)>len(ip2):
    a=len(ip1)
else:
    a=len(ip2)
for i in range (0,a):
    if i>=len(ip1):
        r=r+ip2[i]
    elif i>=len(ip2):
        r=r+ip2[i]
    else:
        r=r+ip1[i]+ip2[i]
print(r)