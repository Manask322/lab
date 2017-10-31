class BinaryHeaps:
	def __init__(self,in_list=[None]*100):
		self.elements=in_list
		self.end=0
		if in_list[0] is None:
			return
		self.elements = [None]+self.elements
		n=len(self.elements)-1
		self.end=len(self.elements)-1
		self.elements+=[None]*200
		for i in range(int(n/2),0,-1):
			self.heapify(i)
	def insert(self,k):
		self.end+=1
		self.elements[self.end]=k
		pi=int(self.end/2)
		i=self.end
		while(pi!=0 and self.elements[pi]>self.elements[i]):
			t=self.elements[i]
			self.elements[i]=self.elements[pi]
			self.elements[pi]=t
			i=pi
			pi//=2
	def maximum(self):
		return self.elements[1]
	def extract_min(self):
		x=self.elements[1]
		t=self.elements[self.end]
		self.elements[self.end]=self.elements[1]
		self.elements[1]=t
		self.elements[self.end]=None
		self.end-=1
		self.heapify(1)
		return x
	def heapify(self,i):
		#print("hello")
		if self.elements[i]==None:
			return
		if self.elements[2*i]==None and self.elements[2*i+1]==None:
			return
		elif self.elements[2*i]!=None and self.elements[2*i+1]==None:
			mini=2*i
		elif self.elements[2*i+1]==None and self.elements[2*i]!=None:
			mini=2*i+1
		else:
			if 2*i>self.end:
				return
			mini=self.elements.index(min(self.elements[2*i+1],self.elements[2*i]))
		if self.elements[mini]<self.elements[i]:
			t=self.elements[mini]
			self.elements[mini]=self.elements[i]
			self.elements[i]=t
			self.heapify(mini)
def main():
	# a=[12,34,5,6,67,90]
	# b=BinaryHeaps()
	# for i in a:
	# 	b.insert(i)
	# # b.display()
	# print(b.extract_max())
	# print(b.extract_max())
	# print(b.extract_max())
	# print(b.extract_max())
	# print(b.extract_max())
	# print(b.extract_max())
	# #print(b.elements[0])
	l=[34,67,68,120, 45,54]
	d=BinaryHeaps(l)
	print("*")
	print(d.extract_min())
	print(d.extract_min())
	print(d.extract_min())
	print(d.extract_min())
	print(d.extract_min())
	print(d.extract_min())
		
if __name__ == '__main__':
	main()


