def fib(n):
	a=0
	b=1
	c=1
	print("0")
	while(c!=n):
		a,b=b,a+b
		print(a)
		c+=1

def fibr(n):
    if(n <= 1):
        return n
    else:
        return(fibr(n-1) + fibr(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibr(i))
print("fib by iteration")
fib(n)








	



