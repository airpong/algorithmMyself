casesize = int(input())
d = [(0,1),(0,-1),(-1,0),(1,0)]     #상 하 좌 우

def move(atoms):
    for atom in atoms:
        atom[0]+=d[atom[2]][0]
        atom[1]+=d[atom[2]][1]
def check(atoms):
    i=0
    global result
    while True:
        flag=0
        if i == len(atoms):
            break
        elif atoms[i][0]<-2000 or atoms[i][0]>2000 or atoms[i][1]<-2000 or atoms[i][1]>2000:
            atoms.pop(i)
        else:
            j=i+1
            while True:
                if j == len(atoms):
                    break
                else:
                    if atoms[i][0]==atoms[j][0] and atoms[i][1]==atoms[j][1]:
                        flag = 1
                        result+=atoms[j][3]
                        atoms.pop(j)
                    else:
                        j+=1
            if flag:
                result+=atoms[i][3]
                atoms.pop(i)
            else:
                i+=1
    if len(atoms)==0:
        return True
for case in range(casesize):
    result = 0
    atomNum = int(input())
    atoms = [list(map(int,input().split())) for _ in range(atomNum)]
    for atom in atoms:
        atom[0]*=2
        atom[1]*=2
    while True:
        move(atoms)
        if check(atoms):
           break
    print(f'#{case+1} {result}')