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
	def minimum(self):
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
			mini=self.elements.index(min(self.elements[2*i+1].distance,self.elements[2*i].distance))
		if self.elements[mini].distance<self.elements[i].distance:
			t=self.elements[mini]
			self.elements[mini]=self.elements[i]
			self.elements[i]=t
			self.heapify(mini)
	def isEmpty(self):
		if self.end==0:
			return True
		else:
			return False
	def updatePriority(self,node):
		i=self.elements.index(node)
		if self.elements[int(i/2)].distance>node.distance:
			t=self.elements[int(i/2)]
			self.elements[int(i/2)]=self.elements[i]
			self.elements[i]=t
			updatePriority(self.elements[int(i/2)])
		else:
			return
# def main():
# 	# a=[12,34,5,6,67,90]
# 	# b=BinaryHeaps()
# 	# for i in a:
# 	# 	b.insert(i)
# 	# # b.display()
# 	# print(b.extract_max())
# 	# print(b.extract_max())
# 	# print(b.extract_max())
# 	# print(b.extract_max())
# 	# print(b.extract_max())
# 	# print(b.extract_max())
# 	# #print(b.elements[0])
# 	l=[34,67,68,120, 45,54]
# 	d=BinaryHeaps(l)
# 	print("*")
# 	print(d.extract_min())
# 	print(d.extract_min())
# 	print(d.extract_min())
# 	print(d.extract_min())
# 	print(d.extract_min())
# 	print(d.extract_min())
#*******************************************************
class node:
	def __init__(self,i):
		self.n=i
		self.colour=None
		self.distance=None
		self.startt=None
		self.endt=None
def adjlist(n,e):
	a=[[] for x in range(n)]
	vertex=[None for x in range(n)]
	for i in range(n):
		vertex[i]=node(i)
	print("Enter edges")
	for i in range(e):
		u,v=tuple(input().split(' '))
		u,v = int(u),int(v)
		a[u].append(v)
		a[v].append(u)
	# for i in range(n):
	# 	print("Vertex ",i,": ",a[i])
	return a,vertex
def dfs(graph,u,time,vlist):
	alist=graph[0]
	vertex=graph[1]
	vertex[u].colour='grey'
	vertex[u].startt=time
	time+=1
	if u not in vlist:
				vlist.append(u)
	for v in alist[u]:
		if not vertex[v].colour=='grey':
			# vlist.append(u)
			dfs(graph,v,time,vlist)
	vertex[u].colour='black'
	vertex[u].endt=time
	time+=1
	return vertex,vlist
def dijkstra(graph,s):
	vertex=graph[0]
	alist=graph[1]
	for u in vertex:
		u.distance=56000
	s.distance=0
	l=[]
	H=BinaryHeaps(vertex)
	while not H.isEmpty():
		w=H.extract_min()
		for v in alist[w.n]:
			if w.distance+d[w.n][v.n]<v.distance:
				v.distance=w.distance+d[w][n]
				H.updatePriority(v)

def main():
	alist,vertex=adjlist(5,6)
	graph=(alist,vertex)
	# print(alist)
	for v in vertex:
		v.colour='white'
	
if __name__ == '__main__':
	main()