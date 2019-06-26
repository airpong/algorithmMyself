# import sys
# sys.stdin = open('input.txt','r')
def bfs():
    # print("bfs시작",startsize,startcol,startrow)
    global time
    tmptime = 0
    while queue:
        # print("나 어디가게?",queue)
        tmplocation = []
        for _ in range(len(queue)):
            tmp = queue.pop(0)
            for i in range(4):
                nextcol = tmp[0]+d[i][0]
                nextrow = tmp[1]+d[i][1]
                if nextcol<0 or nextrow<0 or nextcol>=N or nextrow>=N or visited[nextcol][nextrow]:
                    continue
                if casemap[nextcol][nextrow]!=0 and casemap[nextcol][nextrow]<startsize:
                    if not tmplocation:
                        # print("abcd",casemap[nextcol][nextrow],nextcol,nextrow)
                        tmplocation = [nextcol,nextrow]
                    else:
                        if nextcol<tmplocation[0]:
                            tmplocation = [nextcol,nextrow]
                        elif nextcol==tmplocation[0]:
                            if nextrow<tmplocation[1]:
                                tmplocation = [nextcol,nextrow]
                elif casemap[nextcol][nextrow]==0 or casemap[nextcol][nextrow]==startsize:
                    visited[nextcol][nextrow]=1
                    queue.append((nextcol,nextrow))
        tmptime+=1
        # print("거리1더하기")
        if tmplocation:
            time+=tmptime
            return tmplocation
    return False
        
            
N = int(input())
casemap=[list(map(int,input().split())) for _ in range(N)]
# N = 4
# casemap = [[4,3,2,1],[0,0,0,0],[0,0,9,0],[1,2,3,4]]
startcol = -1
startrow = -1
startsize = 2
time = 0
for col in range(N):
    for row in range(N):
        if casemap[col][row]==9:
            startcol =col;startrow=row
casemap[startcol][startrow]=0
d = [(-1,0),(0,1),(1,0),(0,-1)]
levelup=2
while True:
    visited = [[0]*N for _ in range(N)]
    visited[startcol][startrow]=1
    queue = [(startcol,startrow)]
    tmp = bfs()
    # print("tmpresult",tmp)
    if not tmp:
        break
    startcol = tmp[0];startrow = tmp[1];
    casemap[startcol][startrow]=0
    levelup-=1
    # print("현재 경험치 잔여",levelup)
    if not levelup:
        # print("level up!!")
        startsize+=1
        levelup=startsize
    # print(time)
    # print()
print(time)
