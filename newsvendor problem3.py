import math
Profit = float()
sumProfit=float()
MaxsumProfit=float()
Order=int()

#輸入單位進貨成本c 單位零售價格r 需求的可能個數N 殘值s
c = int(input("清輸入單位進貨成本c:"))
r = int(input("清輸入單位零售價格r:"))
N = int(input("請輸入需求的可能個數N:"))
s = int(input("請輸入殘值s:"))

#輸入賣出個數的機率
ProbabilityStr = input()
#利用空格進行資料剖析
Probability = ProbabilityStr.split(" ")
for i in range(N+1):
	Probability[i] = float(Probability[i])

#j代表訂貨量從0到N
for j in range (N+1):
	for i in range (N+1): #i代表賣出量從0到N
		m = i
		if m > j: #賣出比訂貨多
			m = j
		Profit = ((m * r) - (j * c) + ((j - m) * s)) * Probability[i]
		#print (m * r , "-" , j * c , "+", j - m , "*" , s  ,"*" , Probability[i] , "=" ,Profit) #檢查算式
		#print(Probability[i])
		sumProfit += Profit
	#print(sumProfit) #檢查期望值
	
	if sumProfit > MaxsumProfit:
		MaxsumProfit = sumProfit
		Order = j
		#print("Order=",Order)
	sumProfit = 0 #歸零本次期望值

print(Order, end=" ")
print(math.floor(MaxsumProfit))