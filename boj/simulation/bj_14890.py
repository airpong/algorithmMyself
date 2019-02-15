# caseinfo = list(map(int,input().split()))
# mapArray = [list(map(int,input().split())) for _ in range(caseinfo[0])]
# result = 0
# for col in range(caseinfo[0]):
#     floorList = [0]*caseinfo[0]
#     flag = 1
#     for row in range(caseinfo[0]):
#         if not flag:
#             # print("bf")
#             break
#         elif row == caseinfo[0]-1:
#             # print("에이",col,row)
#             result+=1
        
#         elif mapArray[col][row]==mapArray[col][row+1]:
#             continue
#         elif mapArray[col][row]+1==mapArray[col][row+1]:
#             if row+1-caseinfo[1]<0:    #다음으로 큰수가 나와 계단을 놔야하는데 왼쪽으로 빠지는 경어
#                 flag=0
#                 # print("aa",col,row,floorList)
#                 break
#             else:
#                 floornum=mapArray[col][row]
#                 for floor in range(caseinfo[1]):
#                     if mapArray[col][row-floor]!=floornum:
#                         flag=0
#                         break
#                     elif floorList[row-floor]==0:
#                         floorList[row-floor]=1     #계단 리스트에 계단이 없으면 계단넣어주고 패스
#                         # print('f',col,row,floorList)
#                     else:       #계단이 있으면 빠져나옴
#                         flag=0
#                         # print("ab",col,row,floorList)
#                         break
#         elif mapArray[col][row]==mapArray[col][row+1]+1:
#             if row+caseinfo[1]>=caseinfo[0]:
#                 flag=0
#                 # print("ac",col,row,floorList)
#                 break
#             else:
#                 floornum=mapArray[col][row+1]
#                 for floor in range(1,caseinfo[1]+1):
#                     if mapArray[col][row+floor]!=floornum:
#                         flag=0
#                         break
#                     elif floorList[row+floor]==0:
#                         floorList[row+floor]=1
#                         # print('g',col,row,floorList)
#                     else:
#                         flag=0
#                         # print("ad",col,row,floorList)
#                         break
#         else:
#             flag=0
#             break

# for row in range(caseinfo[0]):
#     floorList = [0]*caseinfo[0]
#     flag = 1
#     for col in range(caseinfo[0]):
#         # print(col,row)
#         if not flag:
#             # print("qmfpr")
#             break
#         elif col == caseinfo[0]-1:
#             # print("b",col,row)
#             result+=1
        
#         elif mapArray[col][row]==mapArray[col+1][row]:
#             # print("gg")
#             continue
#         elif mapArray[col][row]+1==mapArray[col+1][row]:
#             if col+1-caseinfo[1]<0:    #다음으로 큰수가 나와 계단을 놔야하는데 왼쪽으로 빠지는 경어
#                 flag=0
#                 # print("t")
#                 break
#             else:
#                 floornum=mapArray[col][row]
#                 for floor in range(caseinfo[1]):
#                     if mapArray[col-floor][row]!=floornum:
#                         flag=0
#                         # print("y")
#                         break
#                     elif floorList[col-floor]==0:
#                         floorList[col-floor]=1     #계단 리스트에 계단이 없으면 계단넣어주고 패스
#                         # print("u")
#                     else:       #계단이 있으면 빠져나옴
#                         flag=0
#                         # print("q")
#                         break
#         elif mapArray[col][row]==mapArray[col+1][row]+1:
#             if col+caseinfo[1]>=caseinfo[0]:
#                 flag=0
#                 # print("w")
#                 break
#             else:
#                 floornum=mapArray[col+1][row]
#                 for floor in range(1,caseinfo[1]+1):
#                     if mapArray[col+floor][row]!=floornum:
#                         flag=0
#                         # print("Wq")
#                         break
#                     elif floorList[col+floor]==0:
#                         # print("we")
#                         floorList[col+floor]=1
#                     else:
#                         # print("qq")
#                         flag=0
#                         break
# print(result)

