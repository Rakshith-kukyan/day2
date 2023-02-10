def strsum(str, s, n):
	sum = 0
	index = 0
	for i in range(n):
		if (str[i] == s):
			for j in range(len(s)):
				sum += (ord(s[j]) -
						ord('a') + 1)
			index = i + 1
			break
	sum = sum * index
	return sum

# Driver code
str = ["python" ]
s = "python"
n = len(str)
sum = strsum(str, s, n)
print(sum)