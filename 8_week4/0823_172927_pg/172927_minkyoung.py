def solution(picks, minerals):
    # 곡괭이가 끝나서 작업이 종료되는 경우 
    # 캘 수 있는 minerals 까지만 list 자르기 
    if sum(picks) * 5 < len(minerals): 
        minerals = minerals[:sum(picks) * 5]
     
        
    ## 광물을 5개씩 set으로 나누고, 각 set 별로 (작업부하, dia 개수) 계산
    # list_load에 저장
    list_load = []

    while (len(minerals) >= 5):
        load = dia = 0

        for i in range(5):
            if minerals[0] == "diamond":
                load += 25
                dia += 1
            elif minerals[0] == "iron":
                load += 5
            else:
                load += 1
            
            del minerals[0]
        
        list_load.append((load,dia,5))

    # 광물의 개수가 5의 배수가 아닌 경우, 
    # 남은 광물 set 작업부하 계산
    load = dia = 0
    len_remain = len(minerals)

    for i in range(len_remain):
        
        if minerals[0] == "diamond":
            load += 25
            dia += 1
        elif minerals[0] == "iron":
            load += 5
        else:
            load += 1
        
        del minerals[0]
        
    list_load.append((load,dia,len_remain))

    # 한 set의 load에 대해 dia 곡괭이는 5로, iron 곡괭이는 dia * 5 + (5 - dia)로 낮출 수 있음
    # list_load에서 load값이 높은 순으로 좋은 곡괭이를 배치해 tiredness 최소화
    list_load.sort(reverse=True)

    tiredness = 0
    for i in range(len(list_load)):
        if (picks[0]):
            tiredness  += list_load[i][2]
            picks[0] -= 1
        elif (picks[1]):
            tiredness  += list_load[i][1] * 5 + (list_load[i][2] - list_load[i][1])
            picks[1] -= 1
        else:
            tiredness  += list_load[i][0]

    return tiredness

# print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))