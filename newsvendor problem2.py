import math
Profit = float()
sumProfit=float()
MaxsumProfit=float()
Order=int()

c = int(input())
r = int(input())
N = int(input())

ProbabilityStr = input()
Probability = ProbabilityStr.split(" ")

for j in range (1,N):
	q = 0 #宣告賣出數量由0開始
	for i in range(N+1):
		if q > j: #若預期賣出數量大於進貨量 則無貨可賣僅等於進貨量
			q = j
		Profit = ((q * r) - (j * c)) * float(Probability[i])
		#print (q * r , "-" , j * c , "*" , Probability[i] , "=" ,Profit) #檢查算式
		#print(Probability[i])
		sumProfit += Profit
		q += 1
	#print(sumProfit) #檢查期望值
	
	if sumProfit > MaxsumProfit:
		MaxsumProfit = sumProfit
		Order = j
		#print("Order=",Order)
	sumProfit = 0 #歸零本次期望值

print(Order, end=" ")
print(math.floor(MaxsumProfit))