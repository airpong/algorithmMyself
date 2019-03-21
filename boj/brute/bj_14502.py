from itertools import combinations
class queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.allarray = [0]*100
    def push(self,lst):
        self.rear+=1
        self.allarray[self.rear]=lst
    def pop(self):
        if self.front==self.rear:
            return False
        self.front+=1
        return self.allarray[self.front]
        
def solve(casemap,emptylocation,viruslocation):
    global finalresult
    dcnr = [(-1,0),(0,1),(1,0),(0,-1)]
    # flag = 0
    for i,j,k in combinations(emptylocation,3):
        # print(i,j,k)
        # if flag==1:
        #     break
        # flag+=1
        casemap[i[0]][i[1]]=1
        casemap[j[0]][j[1]]=1
        casemap[k[0]][k[1]]=1
        tmp = checkarea(casemap,viruslocation,dcnr)
        if tmp<finalresult:
            finalresult = tmp
        casemap[i[0]][i[1]]=0
        casemap[j[0]][j[1]]=0
        casemap[k[0]][k[1]]=0

def spread(c,r,queueobj,casemap,visited):
    # print(visited)
    count = 0
    for d in [(-1,0),(0,1),(1,0),(0,-1)]:
        nextcol = c+d[0];nextrow = r+d[1]
        if nextcol < 0 or nextrow < 0 or nextcol >= col or nextrow >= row:
            continue
        if casemap[nextcol][nextrow]==0 and not visited[nextcol][nextrow]:
            visited[nextcol][nextrow]=1
            count+=1
            queueobj.push((nextcol,nextrow))
    return count
                    
def checkarea(casemap,viruslocation,dcnr):
    count = 0
    queueobj = queue()
    visited = [[0]*row for _ in range(col)]
    for i in viruslocation:
        queueobj.push(i)
    while True:
        tmp = queueobj.pop()
        # print(tmp)
        if not tmp:
            break
        count += spread(tmp[0],tmp[1],queueobj,casemap,visited)
    del queueobj
    return count
        

col,row = map(int,input().split())
casemap = [list(map(int,input().split())) for _ in range(col)]
finalresult = 987654321
emptylocation = []
viruslocation = []
for c in range(col):
    for r in range(row):
        if casemap[c][r]==0:
            emptylocation.append((c,r))
        elif casemap[c][r]==2:
            viruslocation.append((c,r))
solve(casemap,emptylocation,viruslocation)
print(len(emptylocation)-finalresult-3)
