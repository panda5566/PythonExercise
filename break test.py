a = 1
b = 1

while a <= 10:
	while b <= 10:
		if b == 5:
			break
		print("a*b:", a * b)
		b += 1
	a += 1
print(a)