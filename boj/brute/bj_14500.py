def issafe(location,col,row,visited):
    if location[0]<0 or location[0]>=col or location[1]<0 or location[1]>=row or visited[location[0]][location[1]]!=0:
        return False
    else:
        return True
def pointcheck(location,col,row,casemap,visited,pos,tmpsum,dcnr):
    global maxresult
    tmpsum+=casemap[location[0]][location[1]]
    if pos>=4:
        if tmpsum>maxresult:
            maxresult=tmpsum
    else:
        for i in range(4):
            nextpoint = (location[0]+dcnr[i][0],location[1]+dcnr[i][1])
            if issafe(nextpoint,col,row,visited):
                visited[location[0]][location[1]]=1
                pointcheck(nextpoint,col,row,casemap,visited,pos+1,tmpsum,dcnr)
                visited[location[0]][location[1]]=0
        
def exceptcheck(location,casemap,col,row):
    global maxresult
    if location[0]<col-1 and location[1]<row-2:
        exceptsum = casemap[location[0]][location[1]]+casemap[location[0]][location[1]+1]+casemap[location[0]][location[1]+2]+casemap[location[0]+1][location[1]+1]
        if exceptsum>maxresult:
            maxresult=exceptsum
    if location[0]>0 and location[1]<row-2:
        exceptsum = casemap[location[0]][location[1]]+casemap[location[0]][location[1]+1]+casemap[location[0]][location[1]+2]+casemap[location[0]-1][location[1]+1]
        if exceptsum>maxresult:
            maxresult=exceptsum
caseinfo = list(map(int,input().split()))
casemap = [list(map(int,input().split())) for _ in range(caseinfo[0])]
visited = [[0]*caseinfo[1] for _ in range(caseinfo[0])]
maxresult = -1
dcnr = [(-1,0),(0,1),(1,0),(0,-1)]
for col in range(caseinfo[0]):
    for row in range(caseinfo[1]):
        pointcheck((col,row),caseinfo[0],caseinfo[1],casemap,visited,1,0,dcnr)
        exceptcheck((col,row),casemap,caseinfo[0],caseinfo[1])
print(maxresult)