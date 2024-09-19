num = int(input())
list = list(input())
R = 0
B = 0
cnt = 0
awr = []
#오른쪽으로 R 보내는 경우
for i in list:
    if i == 'R':
        R += 1
    if i == 'B' and R:
        cnt += R
        R = 0
awr.append(cnt)
cnt = 0
B = 0
R = 0
#오른쪽으로 B 보내는 경우
for i in list:
    if i == 'B':
        B += 1
    if i == 'R' and B:
        cnt += B
        B = 0
awr.append(cnt)
cnt = 0
B = 0
R = 0
#왼쪽으로 R 보내는 경우
list.reverse()
for i in list:
    if i == 'R':
        R += 1
    if i == 'B' and R:
        cnt += R
        R = 0
awr.append(cnt)
cnt = 0
B = 0
R = 0
#왼쪽으로 B 보내는 경우
for i in list:
    if i == 'B':
        B += 1
    if i == 'R' and B:
        cnt += B
        B = 0
awr.append(cnt)

print(min(awr))