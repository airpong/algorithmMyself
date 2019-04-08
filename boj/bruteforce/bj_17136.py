def changmap(col,row,hm,num):
    tmp = []
    for c in range(col,col+hm):
        for r in range(row,row+hm):
            if c>=10 or r>=10 or casemap[c][r]==num:
                for i in tmp:
                    casemap[i[0]][i[1]]=match[num]
                return False
            casemap[c][r]=num
            tmp.append((c,r))
    return True
def dfs(pos):
    global result
    if pos>=result:
        return
    flag = False
    for col in range(10):
        for row in range(10):
            if casemap[col][row]==1:
                flag = True
                break
        if flag:
            break
    if not flag:
        if pos<result:
            result = pos
            return
    for i in range(5,0,-1):
        if papers[i]:
            papers[i]-=1
            if changmap(col,row,i,0):
                dfs(pos+1)
                changmap(col,row,i,1)
            papers[i]+=1
    
    

casemap = [list(map(int,input().split())) for _ in range(10)]
result = 30
papers = [0,5,5,5,5,5]
match = [1,0]
dfs(0)
if result == 30:
    print(-1)
else:
    print(result)