from itertools import combinations
N = int(input())
score = []
for i in range(N):
    score.append(list(map(int, input().split())))

players = list(range(N))
half = N // 2
minV = 100000
real_score = []

for a_team in combinations(players, half):
    b_team = list(set(players) - set(a_team))


    a_score = 0
    for i in a_team:
        for j in a_team:
            if i != j:
                a_score += score[i][j]
                
    b_score = 0
    for i in b_team:
        for j in b_team:
            if i != j:
                b_score += score[i][j]
    minV = min(minV, abs(a_score - b_score))
    if minV == 0:
        break
        
print(minV)
