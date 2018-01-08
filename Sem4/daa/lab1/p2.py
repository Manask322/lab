n=5
men_pref=[[] for _ in range(n)]
w_pref=[[] for _ in range(n)]
with open("input.txt",'r') as file:
    lines=file.readlines()
    men=lines[0].split()
    women=lines[1].split()
    for i in range(2,7):
        men_pref[i-2].append(lines[i].split()[1:])
    for i in range(7,len(lines)):
        w_pref[i-7].append(lines[i].split()[1:])
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
    print(men_pref)
    print(w_pref)