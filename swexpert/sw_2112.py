def DFS(films,level,start,W,D,K,pos):
    global result
    if pos==level:
        a=check(films,W,D,K)
        if a:
            result = 1
            return
    else:
        for depth in range(start,D):
            tmp = films[depth]
            for i in range(2):
                films[depth]=[i]*W
                DFS(films,level,depth+1,W,D,K,pos+1)
                if result:
                    return
            films[depth]=tmp
def check(films,W,D,K):
    for row in range(W+1):
        if row == W:
            return True
        else:
            count=1
            before = films[0][row]
            for col in range(1,D+1):
                if col == D:
                    return False
                elif films[col][row]==before:
                    count+=1
                    if count>=K:
                        break
                else:
                    count=1
                    before=films[col][row]
        
    
casesize = int(input())
for case in range(casesize):
    D,W,K = map(int,input().split())
    films = [list(map(int,input().split())) for _ in range(D)]
    result = 0
    if K==1:
        print(f'#{case+1} {result}')
    else:
        for level in range(K+1):
            if level==K:
                print(f'#{case+1} {level}')
            else:
                DFS(films,level,0,W,D,K,0)
                if result==1:
                    print(f'#{case+1} {level}')
                    break

