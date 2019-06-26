def spread(col,row,union,visited,bythis):
    for i in range(4):
        nextcol = col+d[i][0]
        nextrow = row + d[i][1]
        if nextcol>=0 and nextrow >= 0 and nextcol < N and nextrow < N:
            if L<=abs(casemap[nextcol][nextrow]-casemap[col][row])<=R:
                if visited[nextcol][nextrow]!=-1 and visited[nextcol][nextrow] != bythis:
                    visited[nextcol][nextrow]=bythis
                    union[bythis][0]+=casemap[nextcol][nextrow]
                    union[bythis][1]+=1
                    spread(nextcol,nextrow,union,visited,bythis)
                elif visited[nextcol][nextrow]==-1:
                    visited[nextcol][nextrow]=bythis
                    union[bythis][0]+=casemap[nextcol][nextrow]
                    union[bythis][1]+=1
def bfs(queue,visited,idx):
    while queue:
        tmp = queue.pop()
        col=tmp[0];row=tmp[1]
        for i in range(4):
            nextcol = col+d[i][0]
            nextrow = row + d[i][1]
            if nextcol>=0 and nextrow >= 0 and nextcol < N and nextrow < N:
                if L<=abs(casemap[nextcol][nextrow]-casemap[col][row])<=R and not visited[col][row]:
                    visited[col][row]=1
                    union[idx][0]+=casemap[nextcol][nextrow]
                    union[idx][1]+=1
                    queue.append((col.row))
                    
def check(union,visited):
    idx = 0
    for col in range(N):
        for row in range(N):
            if visited[col][row]==0:
                union.append([casemap[col][row],1])
                # print(col,row,union)
                visited[col][row]=1
                bfs(queue,visited,idx)
                idx+=1
                queue=[(col,row)]
                
                print("abcd",col,row,visited)
            # spread(col,row,union,visited,visited[col][row])
                
                    
def solve():
    result = 0
    while True:
        union = []
        visited = [[0]*N for _ in range(N)]
        check(union,visited)
        print("visi",visited)
        print(union)
        if len(union)>=N*N:
            break
        result+=1
        for col in range(N):
            for row in range(N):
                casemap[col][row]=union[visited[col][row]][0]//union[visited[col][row]][1]
        # print(casemap)
    return result
d = [(0,1),(1,0),(0,-1),(-1,0)]
N,L,R = map(int,input().split())
casemap = [list(map(int,input().split())) for _ in range(N)]
print(solve())