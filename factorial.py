def fact(n):
	if (n == 1):
		return n
	else:
		return n*fact(n-1)
n=int(input("enter a number"))
fact=fact(n)
print(fact)
