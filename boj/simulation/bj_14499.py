global col
global row
def movedice(nowcol,nowrow,order,dice,maparray):
    # print("global",col,row)
    print("abc",nowcol,nowrow,order,dice,maparray,sep="-")
    if order == 1:
        if (nowrow+1)>row:
            return False
        else :
            if maparray[nowcol][nowrow+1]==0:
                maparray[nowcol][nowrow+1]=dice[2]
            else:
                dice[2]=maparray[col][nowrow+1]
                maparray[nowcol][nowrow+1]=0
            dice=[dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
            return True,nowcol,nowrow+1,dice
    elif order == 2:
        if (nowrow-1)<0:
            return False
        else :
            if maparray[nowcol][nowrow-1]==0:
                maparray[nowcol][nowrow-1]=dice[3]
            else:
                dice[3]=maparray[nowcol][nowrow-1]
                maparray[nowcol][nowrow-1]=0
            dice=[dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
            return True,nowcol,nowrow-1,dice
    elif order == 3:
        if (nowcol-1)<0:
            return False
        else :
            if maparray[nowcol-1][nowrow]==0:
                maparray[nowcol-1][nowrow]=dice[1]
            else:
                dice[1]=maparray[nowcol-1][nowrow]
                maparray[nowcol-1][nowrow]=0
            dice=[dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
            return True,nowcol-1,nowrow,dice
    elif order == 4:
        if (nowcol+1)>col:
            return False
        else :
            if maparray[nowcol+1][nowrow]==0:
                maparray[nowcol+1][nowrow]=dice[4]
            else:
                dice[4]=maparray[nowcol+1][nowrow]
                maparray[nowcol+1][nowrow]=0
                # print("a",dice)
            dice=[dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
            # print("b",dice)
            return True,nowcol+1,nowrow,dice

caseinfo = list(map(int,input().split()))
col = caseinfo[0]-1
row = caseinfo[1]-1
maparray = [list(map(int,input().split())) for _ in range(caseinfo[0])]
orderList = list(map(int,input().split()))
dice=[0,0,0,0,0,0]
mycol,myrow = caseinfo[2],caseinfo[3]
for order in orderList:
    result = movedice(mycol,myrow,order,dice,maparray)
    if result:
        mycol = result[1]
        myrow = result[2]
        dice = result[3]
        # print(mycol,myrow,dice)
        print(dice[0])