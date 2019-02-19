def move(mapsize,snake,apple,dirch):
    change = 0
    maxchange = len(dirch)-1
    # print(maxchange)
    pos = 0
    idx = 0
    while True:
        pos+=1
        # print(pos)
        lenofsnake = len(snake)
        newcol=snake[lenofsnake-1][0]+dc[idx]
        newrow=snake[lenofsnake-1][1]+dr[idx]
        ck = check(newcol,newrow,mapsize,snake,apple)
        if ck == 0 :        #아무것도없음
            snake.append([newcol,newrow])
            snake.pop(0)
        elif ck == 1:       #사과있음
            snake.append([newcol,newrow])
        elif ck == 2:       #벽또는 자신
            # print('break')
            break
        if str(pos) == dirch[min(change,maxchange)][0]:
            # print("change dir into",dirch[change][1])
            if dirch[change][1]=='D':
                idx+=1
                if idx>=4:
                    idx=0
            if dirch[change][1]=='L':
                idx-=1
                if idx<=-1:
                    idx=3
            change+=1
        # print(snake)
    return (pos)

def check(col,row,mapsize,snake,apple):
    if col < 1 or row < 1 or col > mapsize or row > mapsize or [col,row] in snake:
        return 2
    elif [col,row] in apple:
        apple[apple.index([col,row])] = -1
        return 1
    else:
        return 0

mapsize = int(input())
applecount = int(input())
appleloca = [list(map(int,input().split())) for _ in range(applecount)]
dirchcount = int(input())
dirch = [list(input().split()) for _ in range(dirchcount)]
dc = [0,1,0,-1]     #delta 우,하,좌,상
dr = [1,0,-1,0]
snake = [[1,1]]
print(move(mapsize,snake,appleloca,dirch))