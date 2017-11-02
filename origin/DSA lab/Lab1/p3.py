def isprime(n):
	if n==0:
		print("Enter a number graeter than zero")
	elif(n==1):
		return False
	elif(n==2):
		return True
	else:
		t=0
		for i in range(2,n):
			if n%i==0:
				t=t+1
		if(t==0):
			return True
		else:
			return False
n=int(input("Enter a number"))
if(isprime(n)):
	print("It is a Prime")
elif(n!=0):
	print("It is not a prime")