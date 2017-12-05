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
		self.tree_edge=[]
		self.back_edge=[]
		self.front_edge=[]
		self.cross_edge=[]
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
			# a[v].append(u)
		# for i in range(n):
		# 	print("Vertex ",i,": ",a[i])
		return a,vertex
	def dfs(self,graph,u,vlist):
		alist=graph[0]
		vertex=graph[1]
		vertex[u].colour='grey'
		vertex[u].startt=self.time
		self.time+=1
		vlist.append(u)
		# if u not in vlist:
		# 			vlist.append(u)
		for v in alist[u]:
			if vertex[v].colour=='white': 
				edge=str(u)+"-"+str(v)
				self.tree_edge.append(edge) 
				#add to tree wdge list
				self.dfs(graph,v,vlist)
			else:
				#if adj node start stop time is not over then back edge
				if vertex[v].endt==None :
					edge=str(u)+"-"+str(v)
					self.back_edge.append(edge)
				#if adj node end time grater than start time of this node and 
				elif  vertex[u].startt < vertex[v].startt:
					edge=str(u)+"-"+str(v)
					self.front_edge.append(edge)
				else:
					edge=str(u)+"-"+str(v)
					self.cross_edge.append(edge)
		vertex[u].colour='black'
		vertex[u].endt=self.time
		self.time+=1
		return vertex,vlist,self.tree_edge,self.back_edge,self.front_edge,self.cross_edge
def main():
	g1=g()
	alist,vertex=g1.adjlist(8,12)
	graph=(alist,vertex)
	print(alist)
	for v in vertex:
		v.colour='white'
	vlist=[]
	time=1
	vertex,vlist,tree_edge,back_edge,front_edge,cross_edge=g1.dfs(graph,1,vlist)
	for v in vertex:
		print("vertex",v.n," : ",v.startt,v.endt)
	print(vlist)
	print(tree_edge)
	print(front_edge)
	print(back_edge)
	print(cross_edge)
if __name__ == '__main__':
	main()