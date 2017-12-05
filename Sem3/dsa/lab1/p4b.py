n=int(input("Enter the size of the array"))
a=[None]*n
print("Enter the elements")
for i in range(0,n):
	a[i]=int(input(""))
#for i in range(0,n):
#	print(a[i])
for i in range(0,n):
	for j in range(n-1,i,-1):
		if(a[j]<a[j-1]):
			t=a[j]
			a[j]=a[j-1]
			a[j-1]=t
print(a)
#or i in range( len( A ) ):
##     if ( A[k] < A[k - 1] ):