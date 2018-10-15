import math

Profit = float()
sum = float()

c = int(input())
r = int(input())
N = int(input())
q = int(input())


for i in range(N+1):
	if i > q:
		i = q
	Probability = float(input())
	Profit = ((i * r) - (q * c)) * Probability
	sum += Profit
	print (i * r , "-" , q * c , "*" , Probability , "=" ,Profit)
	print (sum)
	i += 1
	
if sum < 0:
	sum = 0

print (math.floor(sum))