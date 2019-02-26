def makecameradir(camerainfo,pos,depth,fulldir,cameras):
    print("start",pos,fulldir)
    if pos==depth:
        print("*-*",fulldir,cameras)
        expand(fulldir,cameras,casemap)
        return
    else:
        for i in range(camerainfo[cameras[pos][1]][1]):     #cameras = [[(c,r),카메라종류]] / camerainfo = [(초기방향,회전횟수)]
             direc=plus(camerainfo[cameras[pos][1]][0],i)
             fulldir[pos]=direc
             makecameradir(camerainfo,pos+1,depth,fulldir,cameras)

def plus(tup,innt):
    tmp=tup.copy()
    for i in range(len(tup)):
        tmp[i]=(tup[i]+innt)%4
    return tmp
def expand(fulldir,cameras,casemap):
    
    pass

col,row = map(int,input().split())
camerainfo = [(),[[0],4],[[0,2],2],[[0,1],4],[[0,1,2],4],[[0,1,2,3],1]]
casemap = [list(map(int,input().split())) for _ in range(col)]
cameras = []
 
for c in range(col):
    for r in range(row):
        if casemap[c][r]>0 and casemap[c][r] < 6 :
            cameras.append([(c,r),casemap[c][r]])
makecameradir(camerainfo,0,3,[0,0,0],cameras)