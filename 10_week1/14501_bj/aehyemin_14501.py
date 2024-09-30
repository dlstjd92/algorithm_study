# #bottom - up
# N = int(input())
# #디피는 아무리풀어도 모르겟어
# schedule = []
# for i in range(N): 
#    schedule.append(list(map(int, input().split())))
   
# dp = [0 for i in range(N+1)] #일했을 때 얻을수있는 최대 수익

# for i in range(N):
#    for j in range(i+schedule[i][0], N+1):
#       if dp[j] < dp[i] + schedule[i][1]:
#          dp[j] = dp[i] + schedule[i][1]
# print(dp[-1])


#top - down
N = int(input())
schedule = []
for i in range(N): 
   schedule.append(list(map(int, input().split())))
dp = [0 for i in range(N+1)] #일했을 때 얻을수있는 최대 수익

for i in range(N-1, -1, -1):
   #i일에 상담을 하는것이 퇴사일을 넘기면 상담을 하지 않는다
   if i+schedule[i][0] > N:
      dp[i] = dp[i+1]
   else :
      #i일에 상담을 하는 것과 상담을 안하는 것중 큰 것을 선택
      dp[i] = max(dp[i+1], schedule[i][1] + dp[i + schedule[i][0]])
print(dp[0])

   
   