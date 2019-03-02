def check(location,charges):
    candidate = []
    for i in range(len(charges)):
        if abs(charges[i][0]-location[0])+abs(charges[i][1]-location[1])<=charges[i][2]:
            candidate.append(i)
    return candidate
def givemax(acandidate,bcandidate,charges):
    charges.append([100,100,0,0])
    acandidate.append(-1)
    bcandidate.append(-1)
    whatmax=0
    for i in acandidate:
        tmpsum=0
        tmpsum+=charges[i][3]
        for j in bcandidate:
            if j!=i:
                tmpsum+=charges[j][3]
                if tmpsum>whatmax:
                    whatmax=tmpsum
                tmpsum-=charges[j][3]
    charges.pop()
    return whatmax
        
casesize = int(input())
d=[(0,0),(-1,0),(0,1),(1,0),(0,-1)]     #그대로 상 우 하 좌
for case in range(casesize):
    moveNum , chargeNum = map(int,input().split())
    amove = list(map(int,input().split()))
    bmove = list(map(int,input().split()))
    charges = []
    for charge in range(chargeNum):
        tmp = list(map(int,input().split()))
        # print(tmp)
        tmp = [tmp[1]-1,tmp[0]-1,tmp[2],tmp[3]]
        charges.append(tmp)
    alocation = [0,0]
    blocation = [9,9]
    result = 0
    for move in range(moveNum+1):
        # print(move)
        # print("0",alocation,blocation)
        acandidate = check(alocation,charges)
        bcandidate = check(blocation,charges)
        # print("1",acandidate,bcandidate)
        result+=givemax(acandidate,bcandidate,charges)
        # print("3",result)
        if move == moveNum:
            break
        alocation=[alocation[0]+d[amove[move]][0],alocation[1]+d[amove[move]][1]]
        blocation=[blocation[0]+d[bmove[move]][0],blocation[1]+d[bmove[move]][1]]
    
    print(result)