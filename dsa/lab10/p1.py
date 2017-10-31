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
	time+=1
	vertex[u].endt=time
	return vertex,vlist
def main():
	alist,vertex=adjlist(5,6)
	graph=(alist,vertex)
	# print(alist)
	for v in vertex:
		v.colour='white'
	vlist=[]
	time=1
	vertex,vlist=dfs(graph,0,time,vlist)
	for v in vertex:
		print("vertex",v.n," : ",v.startt,v.endt)
	print(vlist)
if __name__ == '__main__':
	main()