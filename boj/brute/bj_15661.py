from itertools import combinations
peapleNum = int(input())
snerge = [list(map(int,input().split())) for _ in range(peapleNum)]
Min = 10000000
for ateam in combinations(range(peapleNum),peapleNum//2):
    ascore = 0
    bscore = 0
    # print(ateam)
    for col in range(peapleNum):
        for row in range(peapleNum):
            # print(col,row)
            if col == row:
                continue
            elif col in ateam and row in ateam:
                ascore+=snerge[col][row]
                # print('a',ascore)
            elif not col in ateam and not row in ateam:
                bscore+=snerge[col][row]
                # print('b',bscore)
    if abs(ascore-bscore)<Min:
        Min = abs(ascore-bscore)
print(Min)
