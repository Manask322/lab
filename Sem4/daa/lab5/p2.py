def min_sem(edges,in_edges,sources=[],sem=[]):
	while(len(sources)!=0):
		sem.append(list(sources))
		for s in sources:
			sources.remove(s)
			for v in edges[s]:
				try:
					in_edges[v]-=1
				except:
					print(len(in_edges))
					print(v)
					return
				if in_edges[v]==0:
					sources.append(v)
	return sem
def main():
	edges=[[1,2],[3],[],[4,5],[],[]]
	in_edges=[0 for i in range(len(edges))]
	for edge in edges:
		for v in edge:
			in_edges[v]+=1
	sources=[]
	for i in range(len(in_edges)):
		if in_edges[i]==0:
			sources.append(i)
	sem=min_sem(edges,in_edges,sources)
	print(len(sem))
if __name__ == '__main__':
	main()