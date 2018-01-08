def pref(n):
	# self.free_men=[None for _ in range(n)]
	# self.wife=[None for _ in range(n)]
	# self.husband=[None for _ in range(n)]
	man_pref=[[] for _ in range(n)]
	w_pref=[[] for _ in range(n)]
	women_pref=[[] for _ in range(n)]
	# for i in range(n):
	# 	print("Enter pref for man ",i)
	# 	for j in range(n):
	# 		p=int(input(""))
	# 		man_pref[i].append(p)
	# print("Women")
	# for i in range(n):
	# 	print("Enter pref for woman ",i)
	# 	for j in range(n):
	# 		p=int(input(""))
	# 		w_pref[i].append(p)
	man_pref=[[1,0,3,4,2],[3,1,0,2,4],[1,4,2,3,0],[0,3,2,1,4],[1,3,0,4,2]]
	w_pref=[[4,0,1,3,2],[2,1,3,0,4],[1,2,3,4,0],[0,4,3,2,1],[3,1,4,2,0]]
	for i in range(n):
		for j in range(n):
			# m=self.w_pref[i][j]
			m=w_pref[i].index(j)
			women_pref[i].append(m)
	return man_pref,women_pref
def main():
	n=int(input("Enter n"))
	man_pref,women_pref=pref(n)
	wife=[None for _ in range(n)]
	husband=[None for _ in range(n)]
	# free_men=[i for i in range(n)]
	free_men=[0,1,2,3,4]
	proposal_count=[0 for i in range(5)]
	m=free_men.pop(0)
	while(len(free_men)!=0):
		# m=free_men.pop(0)
			# print(m)
		proposal_count[m]+=1
		if proposal_count[m]>=5:
			break
		w=man_pref[m][proposal_count[m]]
		if husband[w]==None:
			husband[w]=m
			wife[m]=w
			# print("man:",m,"women:",w,"are engaged")
		elif husband[w]!=None:
			h=husband[w]
			if(women_pref[w][m]<women_pref[w][h]):
				husband[w]=m
				wife[m]=w
				free_men.append(h)
				# print("man:",m,"women:",w,"are engaged 2")
			else:
				free_men.append(m)
		m=free_men.pop(0)
	for i in range(n):
		print("wife: ",i,"husband : ",husband[i])
if __name__ == '__main__':
	main()