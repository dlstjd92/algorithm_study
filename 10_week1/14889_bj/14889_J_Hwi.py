N = int(input())
human = []

for i in range(N):
    human.append(list(map(int, input().split())))


visited = [0] * N

min_A = 100

# 능력치 재는 함수
def ch_ABILITY(team):
    avility = 0
    for i in team:
        for j in team:
            if i != j:
                absility += human[i][j]
    return absility

def backtrack(idx, count):
    global min_A

    # 절반 나눴으면 팀 완성~
    if count == N // 2:
        S_TEAM = []
        L_TEAM = []

        for i in range(N):
            if visited[i]:
                S_TEAM.append(i)
            else:
                L_TEAM.append(i)
        
        # 각 팀 능력치 계산
        S_AVILITY = ch_ABILITY(S_TEAM)
        L_AVILITY = ch_ABILITY(L_TEAM)

        # 능력치 차 최소값
        min_A = min(min_A, abs(S_AVILITY - L_AVILITY))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited [i] = 1
            backtrack(i + 1, count + 1)
            visited[i] = 0

backtrack(0,0)

print(min_A)