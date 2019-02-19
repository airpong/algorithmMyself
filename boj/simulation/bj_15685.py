def drawdragon(dragonList,casemap,dx,dy):
    # print("시행",dragonList)
    tmplist=[dragonList[-1]]
    for line in range(len(dragonList)-1):
        # print("draw함수 인자확인",line,dragonList,dragonList[-1-line],dragonList[-2-line])
        tmpdir = checkdir(dragonList[-1-line],dragonList[-2-line],dx,dy)
        newX = tmplist[-1][0]+dx[tmpdir]
        newY = tmplist[-1][1]+dy[tmpdir]
        tmplist.append((newX,newY))
        casemap[newY][newX]=1
        # print("tmplist확인",tmplist)
    return dragonList+tmplist[1:]
def checkanswer(casemap,result):
    for col in range(100):
        for row in range(100):
            if casemap[col][row]==1 and casemap[col+1][row]==1 and casemap[col][row+1]==1 and casemap[col+1][row+1]==1:
                result +=1
    return result
def checkdir(firstloca,secondloca,dx,dy):
    # print("check함수 인자확인",firstloca,secondloca)
    chx = firstloca[0]-secondloca[0]
    chy = firstloca[1]-secondloca[1]
    for i in range(4):
        # print("이동확인",chx,chy)
        # print(dx[i],dy[i])
        if chx == dx[i] and chy == dy[i]:
            # print("find!",i+1 if i+1<4 else 0)
            return i+1 if i+1<4 else 0

casemap = [[0] * 101 for _ in range(101)]
curvenum = int(input())
dragoncurve = [list(map(int,input().split())) for _ in range(curvenum)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]     #우 상 좌 하
result = 0
for dragon in dragoncurve:
    startpoint = (dragon[0],dragon[1])
    endpoint = (dragon[0]+dx[dragon[2]],dragon[1]+dy[dragon[2]])
    dragonList = [startpoint,endpoint]
    casemap[startpoint[1]][startpoint[0]]=1
    casemap[endpoint[1]][endpoint[0]]=1
    for generation in range(dragon[3]):
        dragonList=drawdragon(dragonList,casemap,dx,dy)
result = checkanswer(casemap,result)
print(result)