N = int(input())
score = int(0)
sum_score = int(0)
for _ in range(N):
    OX = list(input().strip())
    for i in OX:
        if(i == "O"):
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)
    sum_score = 0
    score = 0
