a=input("enter the value")
b=input("enter the 2nd value")
c=input("enter the 3rd value")
if a>=b and a>=c:
	largest=a
	if b>=c and b>=a:
		largest=b
else:
	largest=c
	print("largest value is",largest)