def waterout(remainbox,boxs,col,row,d):
    for c in range(col):
        for r in range(row):
            for direction in range(4):
                if boxs[c][r][direction]==-1:
                    continue
                else:
                    targetc = c+1+d[direction][0]
                    targetr = r+1+d[direction][1]
                    tmp=max(boxs[c][r][direction],remainbox[targetc][targetr])
                    if tmp<remainbox[c+1][r+1]:
                        remainbox[c+1][r+1]=tmp
def count(remainbox,col,row):
    count=0
    for c in range(col):
        for r in range(row):
            count+=remainbox[c+1][r+1]
    return count
col,row,height = map(int,input().split())
boxs = [[[-1,-1,-1,-1] for _ in range(row)] for _ in range(col)]
rowhole = [list(map(int,input().split())) for _ in range(col+1)]
for c in range(col):
    for r in range(row):
        boxs[c][r][0]=rowhole[c][r]
        boxs[c][r][2]=rowhole[c+1][r]
colhole = [list(map(int,input().split())) for _ in range(col)]
for c in range(col):
    for r in range(row):
        boxs[c][r][1]=colhole[c][r+1]
        boxs[c][r][3]=colhole[c][r]
remainbox = [[-1]*(row+2)]+[[-1]+[height]*row+[-1] for _ in range(col)]+[[-1]*(row+2)]
d = [(-1,0),(0,1),(1,0),(0,-1)]       #상 우 하 좌
cnt=count(remainbox,col,row)
tmpcnt = -1
while tmpcnt!=cnt:
    waterout(remainbox,boxs,col,row,d)
    tmpcnt=cnt
    cnt=count(remainbox,col,row)
print(cnt)