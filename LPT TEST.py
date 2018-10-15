#read and prepare n, m, and p
n = int(input("Nimber of jobs: "))
m = int(input("Nimber of machines: "))
pStr = input("processing times: ")

p = pStr.split(' ')
for i in range(n):
	p[i] = int(p[i])
	
#machine completion times
loads = [0] * m
assignment = [0] * n

#每個迴圈跑n次
for j in range(n):

	#找到loads最小的那個並且知道他在哪裏
	leastLoadedMachine = 0
	leastLoad = loads[0]
	for i in range(1, m):
		if loads[i] < leastLoad:
			leastLoadedMachine = i
			leastLoad = loads[i]
	
	#schedule a job
	loads[leastLoadedMachine] += p[j]
	assignment[j] = leastLoadedMachine + 1

#result
print("Job assignment: "+ str(assignment))
print("Machine loads: "+ str(loads))
