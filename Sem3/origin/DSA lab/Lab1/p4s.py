n=int(input("Enter the size of the array"))
a=[None]*n
print("Enter the elements")
for i in range(0,n):
	a[i]=int(input(""))
for i in range(0,n):
	for j in range(i+1,n):
		if(a[j]<a[i]):
			t=a[i]
			a[i]=a[j]
			a[j]=t
print(a)

