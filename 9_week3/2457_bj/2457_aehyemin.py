import datetime as dt
N = int(input())
s =[]
cnt = 0
for i in range(N):
    s_mon, s_day, e_mon, e_day =  map(int, input().split())
    s.append((s_mon*100+s_day, e_mon*100+ e_day))
    
s.sort()
end_day = 301
flower = 0

#11월31일을 넘거나 마지막 꽃의 지는날이 제일 빨리 피는 꽃보다 작으면
while (s):
    if (end_day >= 1201 or s[0][0] > end_day) :
        break
    for _ in range(len(s)):
        if end_day >= s[0][0]:
            if flower <= s[0][1]:
                flower = s[0][1]
            s.remove(s[0])
        else :
            break
    end_day = flower
    cnt += 1
    
if end_day < 1201:
    print(0)
else :
    print(cnt)