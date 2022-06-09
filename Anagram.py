x=input("enter string")
y=input("enter string to char")
x=x.lower()
y=y.lower()
x=[i for i in x.split()]
y=[i for i in y.split()]
x.sort()
y.sort()
if(x==y):
	print("entered string is Anagram")
else:
	print("not an Anagram")
