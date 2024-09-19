num = int(input())

f = []
for i in range(num):
    flower = list(map(int, input(). split()))
    f.append(flower)
f.sort()

total = 0
end_of_world = (3, 1)

i = 0
while i < num:
    s_month, s_day, e_month, e_day = f[i]
    if (s_month, s_day) <= end_of_world < (e_month, e_day):
        temp_end = (e_month, e_day)
        while i < num - 1:
            next_s_month, next_s_day, next_e_month, next_e_day = f[i+1]
            if end_of_world < (next_s_month, next_s_day):
                break
            if temp_end < (next_e_month, next_e_day):
                temp_end = (next_e_month, next_e_day)
            i += 1

        total += 1
        end_of_world = temp_end

        if (11, 30) < end_of_world:
            print(total)
            exit(0)
    i += 1
print(0)