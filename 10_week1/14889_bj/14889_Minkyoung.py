# temp0 = []
# for i in range(N//2+1):
#     bucket = temp0[:]
#     bucket.append(list[i])

#     temp1 = bucket[:]
#     for j in range(i+1, N-1):
#         bucket = temp1[:]
#         bucket.append(list[j])

#         temp2 = bucket[:]
#         for k in range(j+1, N):
#             bucket = temp2[:]
#             bucket.append(list[k])
#             result.append(bucket)

def make_team(list, bucket, depth, N, start):
    if depth == N//2:
        team_cases.append(bucket[:])
        return
    
    for i in range(start, N):
        bucket.append(list[i])
        make_team(list, bucket, depth+1, N, i+1)
        bucket.pop()
   
def cal_attribute(team):
    attribute = 0

    for i in range(len(team)):
        for j in range(len(team)):
            attribute += attributes[team[i]][team[j]]

    return attribute
    
    
N = int(input())
attributes = [[int(i) for i in input().split()] for j in range(N)]
players = [i for i in range(N)]

team_cases = []
make_team(players, [], 0, N, 0)

differences = 99
for team_a in team_cases:
    team_b = [i for i in players if i not in team_a]
    
    attribute_a = cal_attribute(team_a)
    attribute_b = cal_attribute(team_b)

    if differences > abs(attribute_a - attribute_b):
        differences = abs(attribute_a-attribute_b)

print(differences)
