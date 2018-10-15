bank1 = int(input())
bank2 = int(input())
money = int(input())


if money <= bank1:
	bank1 = bank1 - money
	bank2 = bank2 + money
else:
	bank2 = bank2 + bank1
	bank1 = bank1 - bank1

print(bank1, bank2)