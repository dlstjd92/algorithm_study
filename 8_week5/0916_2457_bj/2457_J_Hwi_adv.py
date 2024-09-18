num = int(input())

f = [list(map(int, input().split())) for i in range(num)]
f.sort()

total = 0
end_of_world = (3, 1)

i = 0
while i < num and end_of_world <= (11, 30):
    max_end = (0,0)
    while i < num:
        s_month, s_day, e_month, e_day = f[i]
        if (s_month, s_day) > end_of_world:
            break
        if max_end < (e_month, e_day):
            max_end = (e_month, e_day)
        i += 1
    if max_end == (0, 0):
        break
    end_of_world = max_end
    total += 1
if end_of_world > (11, 30):
    print(total)
else:
    print(0)