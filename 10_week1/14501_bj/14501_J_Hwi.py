N = int(input())
scd = []

for i in range(N):
    scd.append(list(map(int, input().split())))
# MAX_PAY = 0
# for i in range(N):
#     j = i
#     sum = 0
#     while j < N:
#         sum += scd[j][1]
#         j += scd[j][0]
#         if j > N:
#             break
#         else:
#             if MAX_PAY < sum:
#                 MAX_PAY  = sum
# print(MAX_PAY)
dp = [0] * (N + 1)

for i in range(N):
    day = scd[i][0]
    pay = scd[i][1]

    if i + day <= N:
        dp[i + day] = max(dp[i + day], dp[i] + pay)
    dp[i + 1] = max(dp[i + 1], dp[i])
print(dp[N])