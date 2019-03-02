inputline = list(input())
i=0
level = 0
result = 0
while i<len(inputline):
    if inputline[i]=='(':
        if inputline[i+1]==')':
            result+=level
            i+=1
        else:
            level+=1
    else:
        level-=1
        result+=1
    i+=1
print(result)