def rotateGear(gearList,gear,direction,which):
    if which == 'All':
        if gear<len(gearList)-1:
            if gearList[gear][2]!=gearList[gear+1][6]:
                rotateGear(gearList,gear+1,-direction,'Right')
        if gear>0:
            if gearList[gear][6]!=gearList[gear-1][2]:
                rotateGear(gearList,gear-1,-direction,'Left')
    elif which == 'Right':
        if gear<len(gearList)-1:
            if gearList[gear][2]!=gearList[gear+1][6]:
                rotateGear(gearList,gear+1,-direction,'Right')
    elif which == 'Left':
        if gear>0:
            if gearList[gear][6]!=gearList[gear-1][2]:
                rotateGear(gearList,gear-1,-direction,'Left')
    if direction == 1 :
        tmp=gearList[gear].pop()
        gearList[gear]=[tmp]+gearList[gear]
    elif direction == -1 :
        tmp=gearList[gear].pop(0)
        gearList[gear].append(tmp)

gearList = [list(map(int,list(input()))) for _ in range(4)]
rotateSize = int(input())
for rotate in range(rotateSize):
    info = list(map(int,input().split()))
    rotateGear(gearList,info[0]-1,info[1],'All')
result=0
for idx,gear in enumerate(gearList):
    if gear[0]:
        result+=2**idx
print(result)

