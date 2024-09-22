N = int(input())
flowers = []

for i in range(N):
    flowers.append([int(j) for j in input().split()])


flowers = sorted(flowers, key = lambda x : (x[0], x[1], x[2], x[3]))
flowers.insert(0,[0,0,3,1])

i = cnt = end = 0
    
while i < N and flowers[i][2] < 12:
    j = i + 1 

    if flowers[j][0] == flowers[i][0] and flowers[j][1] == flowers[i][1]:
        i = j
        continue

    while j < N + 1 and flowers[j][0] < flowers[i][2]:
        if flowers[j][2] > 11:
            end = True
            i = j
            break
        j += 1

    if j < N + 1:
        cnt += 1

        if end: break

        if flowers[j][0] != flowers[i][2] or flowers[j][1] > flowers[i][3]:
            if i == j-1:
                cnt = 0
                break
            i = j-1
        else:
            i = j

    else:
        cnt = 0
        break

if flowers[i][2] == 12:
# print(i)
# if i < N+1:
    print(cnt)
else:
    print(0)

# 3월 1일부터 11월 30일