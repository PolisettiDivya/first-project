def compound(p,t,r):
	ci=p*(pow((1+r/100),t))
	return ci
p=float(input("enter the principal amount"))
r=float(input("enter the rate of interest"))
t=float(input("enter the number of years"))
ci=compound(p,r,t)
print("compound intest :{}".format(ci))

