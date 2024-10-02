def best_schedule(day, schedule, n, dp):
    # 종료 조건: n일을 넘으면 더 이상 상담할 수 없음
    if day >= n:
        return 0
    
    # 이미 계산된 값이 있으면 그 값을 반환 (메모이제이션)
    if dp[day] != -1:
        return dp[day]
    
    t, p = schedule[day]  # t: 상담 기간, p: 상담 이익

    # 상담을 선택하지 않는 경우: 다음 날로 넘어감
    no_consult = best_schedule(day + 1, schedule, n, dp)

    # 상담을 선택하는 경우: 상담이 퇴사일을 넘지 않을 때만
    if day + t <= n:
        consult = p + best_schedule(day + t, schedule, n, dp)
    else:
        consult = 0

    # 최댓값을 dp에 저장하고 반환
    dp[day] = max(no_consult, consult)
    return dp[day]


def best_schedule(schedule, day):
    dp = [0] * (day + 1)
    # n일 까지의 최댓값을 구하는 법
    # 1일부터 하루씩 더하면서
    # 해당일을 넣었을때와 뺏을때를 비교하면서 차례대로 상승
    # 만약 마지막상담과 겹치지 않으면? 무조건 넣는게 이득

    for i in range(day): # day - 1 까지 도는 포문..
        # 오늘의 최선 = 어제까지 최댓값 vs 오늘치를 포함했을 때의 값
        today = schedule[i][0]
        money = schedule[i][1]

        # 내일 값보다 오늘값이 더 높으면? 고
        dp[i+1] = max(dp[i+1],dp[i])

        # 오늘 상담을 했을때 해당 날짜랑 값 비교함
        if i + today <= day:
            dp[i + today] = max(dp[i + today], dp[i] + money)

    return dp

day = int(input())

schedule = []

for i in range(day):
    schedule.append(list(map(int,input().split())))

answer = best_schedule(schedule, day)

print(max(answer))

