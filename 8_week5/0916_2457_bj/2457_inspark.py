import sys

times = int(input())

month = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

flower_list = [[] for _ in range(times)]

# princess = [60,334]

cnt = 0

for j in range(times):
    flower = list(map(int,sys.stdin.readline().split()))
    temp1 = 0
    temp2 = 0

    for i in range(1,flower[0]):
        temp1 += month[i]

    temp1 += flower[1]

    for i in range(1, flower[2]):
        temp2 += month[i]

    temp2 += flower[3]

    flower_list[j] = [temp1, temp2]

sorted_flower = sorted(flower_list, key=lambda x:x[0])

print(sorted_flower)

start = 60
end = 335 # 11월 30일에 시들면 안돼니까 다음날까지 피어있게 해야함!!!!

far_flower = 0

answer = 0

# 시작점을 지속적으로 갱신해서 가장 멀리가는 꽃을 찾기
while(start < end):
    
    while cnt < len(sorted_flower) and sorted_flower[cnt][0] <= start:
        # 최고점 갱신
        far_flower = max(far_flower, sorted_flower[cnt][1])
        cnt+=1

    if far_flower <= start:
        break

    start = far_flower
    answer += 1

    if start >= end:
        break

if start >= end:
    print(answer)
else:
    print(0)

# 생각을 바꿔서... 무조건 겹치게 찾아야함
# temp = sorted_flower.pop()

# if temp[0] <= 60 or temp[1] >= 334:
#     answer.append(temp)

# app_check = 0

# for i in sorted_flower:
#     # 안에 있는지 확인하는 알고리즘
#     # 60 ~ 334랑 
#     if i[0] <= 60 or i[1] >= 334: # 일단 꽃이 범위에 드는가?

#         for j in answer: # 그리고 순회하면서 점수 비교
#             if i[0]<=j[0] or i[1]>=j[1]: #만약 겹치면
#                 # 겹쳐도 됨.. 그러면 겹치는게 문제가 아니라 얼마나 겹치는지를 봐야 하는데..
#             else: # 안겹치면
                


