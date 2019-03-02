global N
global visited
global finalresult
def solve(start,end,nodeconnect,connectlist,flag,pos):
    
N=5
visited=[0,0,0,0,0]
inputmap=[[0,1,0,0,0],[1,0,2,0,0],[0,2,0,3,0],[0,0,3,0,4],[0,0,0,4,0]]
result=[]
finalresult = []
print(solve(2,4,inputmap,result,True,0))

