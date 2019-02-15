global direction
def clean(mycol,myrow,look,pos,maparray,hm):
    # print(mycol,myrow,look,pos,maparray,hm,sep='-')
    left = look-1
    if look-1<0:
        left=3
    lookcol = mycol + direction[left][0]
    lookrow = myrow + direction[left][1]
    # print("왼쪽좌표",lookcol,lookrow)
    if maparray[lookcol][lookrow] ==0:
        # print('0이다!')
        maparray[lookcol][lookrow]=2
        return clean(lookcol,lookrow,left,0,maparray,hm+1)
    else:
        if pos>=4:
            backcol=mycol-direction[look][0]
            backrow=myrow-direction[look][1]
            # print("뒤쪽좌표",backcol,backrow)
            if maparray[backcol][backrow]==1:
                return hm
            else:
                # print("뒤로총총")
                return clean(backcol,backrow,look,0,maparray,hm)
        else:
            return clean(mycol,myrow,left,pos+1,maparray,hm)

direction = [[-1,0],[0,1],[1,0],[0,-1]]
mapsize = list(map(int,input().split()))
caseinfo = list(map(int,input().split()))
maparray = [list(map(int,input().split())) for _ in range(mapsize[0])]
maparray[caseinfo[0]][caseinfo[1]]=2
print(clean(caseinfo[0],caseinfo[1],caseinfo[2],0,maparray,1))