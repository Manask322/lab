def adjmatrix(n,e):
	a = [[0 for x in range(n)] for y in range(n)]
	vertex=[None for x in range(n)]
	for i in range(n):
		vertex[i]=node(i)
	for i in range(e):
		u,v=tuple(input().split(' '))
		u,v = int(u),int(v)
		a[u][v]+=1
		a[v][u]+=1
	for i in range(n):
		for j in range(n):
			print(a[i][j]," ",end='')
		print()
	return a
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
	return a,vertex
class node:
	def __init__(self,i):
		self.n=i
		self.colour='white'
		self.distance=None
def bfs(graph,s):
	alist=graph[0]
	vertex=graph[1]
	for v in vertex:
		if v.n!=s:
			v.distance=56000
			v.colour='white'
	source=vertex[s]
	source.distance=0
	source.colour='gray'
	Q=[]
	vlist=[]
	Q.append(vertex[s])
	vlist.append(vertex[s].n)
	while not len(Q)==0:
		u=Q.pop(0)
		for v in alist[u.n]:
			if vertex[v].colour=='white':
				vertex[v].distance=u.distance+1
				vertex[v].colour='gray'
				vlist.append(vertex[v].n)
				Q.append(vertex[v])
		vertex[u.n].colour='black'
	return vlist
def components(graph):
	vertex=graph[1]
	c=0
	for v in vertex:
		if v.colour=='white':
			vlist=bfs(graph,v.n)
			print(vlist)
			c+=1
	return c
def main():
	alist,vertex=adjlist(6,4)
	graph=(alist,vertex)
	print(components(graph))
if __name__ == '__main__':
	main()