n = int (input())
k = 0
m = 1

while n > m:
	m *= 2
	k += 1

if m == n:
	print(n, "is 2 to the power of", k)
else:
	print(n, "isn't the power of 2") 