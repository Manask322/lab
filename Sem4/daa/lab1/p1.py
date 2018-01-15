def read_from_file(file):
	with open(file,'r') as file:
		lines=file.readlines()
		men=lines[0].split()
		n=len(men)
		women=lines[1].split()
		men_pref=[[] for _ in range(n)]
		w_pref=[[] for _ in range(n)]
		for i in range(2,2+n):
			men_pref[i-2].append(lines[i].split()[1:])
		for i in range(2+n,len(lines)):
			w_pref[i-(2+n)].append(lines[i].split()[1:])
		for i in range(len(men_pref)):
			men_pref[i]=men_pref[i][0]
		for i in range(len(men_pref)):
			w_pref[i]=w_pref[i][0]    
		for i in range(n):
			for j in range(n):
				men_pref[i][j]=women.index(men_pref[i][j])
		for i in range(n):
			for j in range(n):
				w_pref[i][j]=men.index(w_pref[i][j])
	return n,men_pref,w_pref,men,women
def pref():
	n,man_pref,w_pref,men,women=read_from_file("input.txt")
	women_pref=[[] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			m=w_pref[i].index(j)
			women_pref[i].append(m)
	return n,man_pref,women_pref,men,women
def main():
	n,man_pref,women_pref,men_list,women=pref()
	wife=[None for _ in range(n)]
	husband=[None for _ in range(n)]
	free_men=[i for i in range(n)]
	proposal_count=[0 for i in range(5)]
	men=[]
	while(len(free_men)!=0):
		m=free_men.pop(0)
		if proposal_count[m]==5:
			break
		w=man_pref[m][proposal_count[m]]
		if husband[w]==None:
			husband[w]=m
		elif husband[w]!=None:
			h=husband[w]
			if(women_pref[w][m]<women_pref[w][h]):
				husband[w]=m
				free_men.append(h)
			else:
				free_men.append(m)		
		proposal_count[m]+=1
	for i in range(n):
		print("wife: ",women[i],"   husband : ",men_list[husband[i]])
if __name__ == '__main__':
	main()