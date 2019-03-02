def solve(nums,N,tmpsum,plusnum,tmp):
    global result
    if result:
        return
    elif tmpsum>N:
        return
    elif tmpsum==N:
        result=1
        return
    else:
        for i in range(3):
            if nums[i]>=plusnum:
                tmp[i]+=1
                solve(nums,N,tmpsum+nums[i],nums[i],tmp)
                tmp[i]-=1
a,b,c,N = map(int,input().split())
result=0
tmp=[0,0,0]
solve((a,b,c),N,0,a,tmp)
print(result)