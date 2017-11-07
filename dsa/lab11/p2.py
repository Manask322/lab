def mergesort(a,low,high):
	if(low<high):
		mid=int((low+high)/2)
		mergesort(a,low,mid)
		mergesort(a,mid+1,high)
		merge(a,low,mid,high)
def merge(a,low,mid,high):
	a1=[]
	a2=[]
	# a1[i]=a[low:mid+1]
	# a2[i]=a[mid+1:high]
	for i in range(low,mid+1):
		a1.append(a[i])
	for i in range(mid+1,high+1):
		a2.append(a[i])
	print(a1,a2)
	i=0
	j=0
	k=low
	while (i<len(a1) and j<len(a2)):
		if a1[i]<a2[j]:
			a[k]=a1[i]
			i+=1
			k+=1
		else:
			a[k]=a2[j]
			j+=1
			k+=1
	while(i<len(a1)):
		a[k]=a1[i]
		k+=1
		i+=1
	while(j<len(a2)):
		a[k]=a2[j]
		k+=1
		j+=1	
def main():
	a=[56,-7,5,34,0,7,23,9]
	b=[0,1,6,2]
	mergesort(a,0,7)
	mergesort(b,0,3)
	print(b)
	print(a)
if __name__ == '__main__':
	main()