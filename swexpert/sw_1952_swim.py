def nowon(nowmon,months,prices,minmonth):
    # print(nowmon)
    if nowmon<0:
        return 9999
    else :
        a=minmonth[nowmon-1]+months[nowmon]
        b=minmonth[nowmon-2]+(prices[2] if months[nowmon]+months[nowmon-1]>prices[2] else months[nowmon]+months[nowmon-1])
        c=minmonth[nowmon-3]+(prices[2] if months[nowmon]+months[nowmon-1]+months[nowmon-2]>prices[2] else months[nowmon]+months[nowmon-1]+months[nowmon-2])
        # print(a,b,c)
        minmonth[nowmon]=min(a,b,c)
def init(yearplan,prices):
    months = [0]*12
    for i in range(12):
        months[i]=prices[1] if yearplan[i]*prices[0]>prices[1] else yearplan[i]*prices[0]
    return months
casesize = int(input())
for case in range(casesize):
    prices = list(map(int,input().split()))
    yearplan = list(map(int,input().split()))
    months=init(yearplan,prices)
    minmonth = [0]*12
    minmonth[0]=months[0]
    minmonth[1]=prices[2] if months[0]+months[1]>prices[2] else months[0]+months[1]
    for i in range(0,12):
        nowon(i,months,prices,minmonth)
    print(minmonth[11] if minmonth[11]<prices[3] else prices[3])  