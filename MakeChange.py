Money=int()
Change=int()
Money=int(input())
Change=1000-Money
Register500=Change//500
Change=Change%500
Register100=Change//100
Change=Change%100
Register50=Change//50
Change=Change%50
Register10=Change//10
Change=Change%10
Register5=Change//5
Change=Change%5
Register1=Change//1
Change=Change%1
print(Register500,Register100,Register50,Register10,Register5,Register1)