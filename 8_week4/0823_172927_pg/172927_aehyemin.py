import numpy as np

def solution(picks, minerals):#곡괭이개수picks정수배열, 광물들순서minerals문자열배열
    #배열을 다섯개씩 나누었을때 다이아가 가장 많은 곳에 다이아 배정

    energy = [] 
    five = [minerals[i:i+5] for i in range(0, len(minerals), 5)]

    if sum(picks)* 5 < len(minerals) :
        five = five[:sum(picks)]
        
    for i in five :
        weight = 0
        for mineral in i:
            if mineral == "diamond" :
                weight += 25
            elif mineral == "iron" :
                weight += 5
            elif mineral == "stone" :
                weight += 1
        energy.append(weight)
   

    sort_energy= sorted(range(len(energy)), key=lambda i: energy[i], reverse=True)
    total_fatigue = 0

    for i in sort_energy:
        if sum(picks) == 0:
            break
            
        if picks[0] > 0: #다이아몬드 곡괭이
            for mineral in five[i]:
                total_fatigue += 1
            picks[0] -= 1
            
        elif picks[1] > 0: #철 곡괭이
            for mineral in five[i]:
                if mineral == "diamond" :
                    total_fatigue += 5
                else :
                    total_fatigue += 1
            picks[1] -= 1   
            
        elif picks[2] > 0: #돌 곡괭이
            for mineral in five[i]:
                if mineral == "diamond" :
                    total_fatigue += 25
                elif mineral == "iron":
                    total_fatigue += 5
                else :
                    total_fatigue += 1
            picks[2] -= 1   
                
    return total_fatigue
            