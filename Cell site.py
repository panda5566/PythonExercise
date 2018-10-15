import math
axis=[]
newaxis=[] 
sum = int()
maxperson = int()
sumperson = int()

npdStr=input()
npd = npdStr.split(" ")
#n=城鎮的數量 p=要蓋的基地台數目 d=基地台覆蓋距離

for i in range(len(npd)):
	npd[i] = int(npd[i])
#將npd資料分割至各陣列
	
for i in range(npd[0]): #npd第一項=城鎮的數量
	axis.append(input())  #輸入每個點座標資料x,y,人數
	axis[i] = axis[i].split(" ")
	
for m in range(npd[1]):
	for i in range(npd[0]):
		for j in range(npd[0]):
			if ((float(axis[i][0])-float(axis[j][0])) ** 2 + (float(axis[i][1])-float(axis[j][1])) ** 2)** 0.5 <= npd[2]:
				#print("i: ", i, "j: ", j, "  ", axis[j][2]) #檢查i到j城鎮有幾人
				sum += int(axis[j][2])
			#print(((float(axis[i][0])-float(axis[j][0])) ** 2 + (float(axis[i][1])-float(axis[j][1])) ** 2)** 0.5)
		if sum > maxperson:
			maxperson = sum
			maxtown = i
		#print("total person:", sum, "MAXtown:", maxtown+1) #檢查最大人數以及最大覆蓋城鎮
		sum = 0
	print(maxtown+1,"",end='')
		
	for k in range(npd[0]):
		if ((float(axis[maxtown][0])-float(axis[k][0])) ** 2 + (float(axis[maxtown][1])-float(axis[k][1])) ** 2)** 0.5 <= npd[2]:	
			axis[k][2] = 0
	sumperson += maxperson
	maxperson = 0
	#print("-----------------------------")
		
print(sumperson)