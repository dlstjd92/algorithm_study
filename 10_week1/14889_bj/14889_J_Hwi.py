N = int(input())
human = []

for i in range(N):
    human.append(list(map(int, input().split())))


visited = [0] * N

min = 100

# 능력치 재는 함수
def ch_ABILITY(team):
    avility = 0
    for i in team:
        for j in team:
            if i != j:
                absility += human[i][j]
    return absility

