def people_comb(choice,depth):
# 1234 와 1423이 똑같은데.. 중복하지 않는 방법 = 순서가 없는 행렬? 
# -> 그냥 20C10 하는법 검색..
    result = []
    if depth == 0:
        return [[]]

    for i in range(len(choice)):
        pick = choice[i]
        remain = choice[i+1:]
        for comb in people_comb(remain,depth-1):
            result.append([pick] + comb) 

    return result

people = int(input())

power = []

for i in range(people):
    power.append(list(map(int,input().split())))

# 짜야하는건 세가지
# 선수를 무작위로 반반 나누기
# 짜여진 선수에서 점수 계싼하기
# 거기에 백트래킹까지
name = [0] * people
for i in range(people):
    name[i] = i+1
# 한쪽팀 선수만 고르면 반대쪽 팀 선수는 자동으로 걸러짐
# people/2 만큼 숫자뽑기 -> 뎁쓰가 people/2까지의 트리로 결정
# 트리는 재귀로?

comb = people_comb(name,people/2)

min_gap = 9999999

for home_team in comb:
    side_team = []
    for j in name:
        if j not in home_team:
            side_team.append(j)

    home_power=0
    side_power=0

    for j in range(len(home_team)):
        for k in range(len(home_team)):
            # print(j,k, side_team)
            home_power += power[home_team[j]-1][home_team[k]-1]
            side_power += power[side_team[j]-1][side_team[k]-1]
        
    temp_gap = abs(home_power-side_power)

    min_gap = min(temp_gap, min_gap)

print(min_gap)



