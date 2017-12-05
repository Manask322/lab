# public static void sort(double[] a, double[] tmp )
#    {
#       int width;

#       for ( width = 1; width < a.length; width = 2*width )      
#       {
#          // Combine pairs of array a of width "width"
#          int i;

#          for ( i = 0; i < a.length; i = i + 2*width )
#          {
#             int left, middle, right;

#             left = i;
#             middle = i + width;
#             right  = i + 2*width;

#             merge( a, left, middle, right, tmp );

#          }
#       }
#    }
def mergesort(a,low,high):
    width=1
    while(width<len(a)):
        i=0
        while(i<len(a)):
            left,middle,right=i,i+width,i+2*width
            merge(a,left,middle,right,tmp=[])
            i+=2*width
        width=2*width
def mergesort1(a,low,high):
	if(low<high):
		mid=int((low+high)/2)
		mergesort(a,low,mid)
		mergesort(a,mid+1,high)
		merge(a,low,mid,high)
def merge(a,low,mid,high,tmp):
	a1=[]
	a2=[]
	# a1[i]=a[low:mid+1]
	# a2[i]=a[mid+1:high]
	for i in range(low,mid+1):
		a1.append(a[i])
	for i in range(mid+1,high+1):
		a2.append(a[i])
	# print(a1,a2)
	i=0
	j=0
	k=low
	while (i<len(a1) and j<len(a2)):
		if a1[i]<a2[j]:
			tmp[k]=a1[i]
			i+=1
			k+=1
		else:
			tmp[k]=a2[j]
			j+=1
			k+=1
	while(i<len(a1)):
		tmp[k]=a1[i]
		k+=1
		i+=1
	while(j<len(a2)):
		tmp[k]=a2[j]
		k+=1
		j+=1	
	for i in range(low,high,1):
		a[i]=tmp[i]
	return 
def main():
	a=[56,-7,5,34,0,7,23,9]
	b=[0,1,6,2]
	# tmp=[]
	mergesort(a,0,7)
	mergesort(b,0,3)
	print(b)
	print(a)
if __name__ == '__main__':
	main()