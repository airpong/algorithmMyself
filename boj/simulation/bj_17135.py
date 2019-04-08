from copy import deepcopy
def simul():
    # print(shooter)
    while tmpenemy:
        attack()
        # print("remain enemy",tmpenemy)
        for i in range(len(tmpenemy)-1,-1,-1):
            tmpenemy[i][0]=tmpenemy[i][0]+1
            
            if tmpenemy[i][0]>=N:
                del tmpenemy[i]
        # print("After",tmpenemy)
    
def attack():
    global tmpcount
    delgroup = []
    for loca in shooter:
        mindis = 987654321
        minindex = -1
        for ene in range(len(tmpenemy)):
            # print(tmpenemy)
            tmpdis = abs(tmpenemy[ene][0]-loca[0]) + abs(tmpenemy[ene][1]-loca[1])
            if tmpdis<=D and tmpdis<=mindis:
                if tmpdis==mindis:
                    # print(tmpdis,minindex)
                    if tmpenemy[ene][1]<tmpenemy[minindex][1]:
                        mindis = tmpdis
                        minindex = ene
                else:
                    mindis = tmpdis
                    minindex = ene
        if minindex!=-1:
            delgroup.append(minindex)
    # print("abc",delgroup)
    delgroup = sorted(list(set(delgroup)))
    # print("delgroup",delgroup)
    # print("aa",tmpenemy)
    if delgroup:
        tmpcount+=len(delgroup)
        for i in range(len(delgroup)-1,-1,-1):
            del tmpenemy[delgroup[i]]

N,M,D = map(int,input().split())
casemap = [list(map(int,input().split())) for _ in range(N)]+[[0]*M]
result = 0
enemy = []
for col in range(0,N):
    for row in range(M):
        if casemap[col][row]==1:
            enemy.append([col,row])
for i in range(M):
    for j in range(i+1,M):
        for k in range(j+1,M):
            tmpenemy = deepcopy(enemy)
            shooter = [(N,i),(N,j),(N,k)]
            tmpcount = 0
            simul()
            if tmpcount>result:
                result = tmpcount
print(result)