from itertools import combinations
def solve(casemap,emptylocation,viruslocation):
    dcnr = [(-1,0),(0,1),(1,0),(0,-1)]
    for i,j,k in combinations(emptylocation,3):
        casemap[i[0]][i[1]]=1
        casemap[j[0]][j[1]]=1
        casemap[k[0]][k[1]]=1
        checkarea(casemap,viruslocation,dcnr)
        casemap[i[0]][i[1]]=0
        casemap[j[0]][j[1]]=0
        casemap[k[0]][k[1]]=0
def checkarea(casemap,viruslocation,dcnr):
    for i in range()
    pass
col,row = map(int,input().split())
casemap = [list(map(int,input().split())) for _ in range(col)]
emptylocation = []
viruslocation = []
for c in range(col):
    for r in range(row):
        if casemap[c][r]==0:
            emptylocation.append((c,r))
        elif casemap[c][r]==2:
            viruslocation.append((c,r))
solve(casemap,emptylocation,viruslocation)
