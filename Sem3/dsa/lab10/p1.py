class node:
	def __init__(self,i):
		self.n=i
		self.colour=None
		self.distance=None
		self.startt=None
		self.endt=None
class g:
	def __init__(self):
		self.time=1
	def adjlist(self,n,e):
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
	def dfs(self,graph,u,vlist):
		alist=graph[0]
		vertex=graph[1]
		vertex[u].colour='grey'
		vertex[u].startt=self.time
		self.time+=1
		if u not in vlist:
					vlist.append(u)
		for v in alist[u]:
			if vertex[v].colour=='white':
				# vlist.append(u)
				self.dfs(graph,v,vlist)
		vertex[u].colour='black'
		vertex[u].endt=self.time
		self.time+=1
		return vertex,vlist
def main():
	g1=g()
	alist,vertex=g1.adjlist(5,6)
	graph=(alist,vertex)
	# print(alist)
	for v in vertex:
		v.colour='white'
	vlist=[]
	time=1
	vertex,vlist=g1.dfs(graph,0,vlist)
	for v in vertex:
		print("vertex",v.n," : ",v.startt,v.endt)
	print(vlist)
if __name__ == '__main__':
	main()