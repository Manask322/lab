def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
def fact1(n):
	ans=1
	for i in range(1,n+1):
		ans=ans*i
	return ans	
n=int(input("Enter the number"))
print("Answer by recursion:",fact(n))
print("\n Answer by iteration :",fact1(n))    


