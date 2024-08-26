from queue import PriorityQueue

def solution(picks, minerals): #광물이 곡갱이 갯수보댜 많을 때 예외처리 안되어있음.
    V = PriorityQueue()
    answer = 0
    
    fatigue = [0, 0, 0]
    count = 0
    picks_v = (picks[0] + picks[1] + picks[2])*5
    minerals = minerals[:picks_v]
    
    
    for m in minerals:
        
        if m == "diamond":
            fatigue[0] -= 25  # 다이아몬드는 높은 피로도
            fatigue[1] -= 5
            fatigue[2] -= 1
        elif m == "iron":
            fatigue[0] -= 5   # 철은 중간 피로도
            fatigue[1] -= 1
            fatigue[2] -= 1
        else:  # stone
            fatigue[0] -= 1   # 돌은 낮은 피로도
            fatigue[1] -= 1
            fatigue[2] -= 1
            
        count += 1
        if count == 5:  # 5개 단위로 자름
            V.put(tuple(fatigue))
            fatigue = [0, 0, 0]
            count = 0
    
    # 마지막이 5개 이하일 경우 처리
    if count > 0:
        V.put(tuple(fatigue))
    
    # 다이아몬드 곡괭이 배정
    for _ in range(picks[0]):
        if not V.empty():
            fatigue = V.get()
            answer -= fatigue[2]
    
    # 철 곡괭이 배정
    for _ in range(picks[1]):
        if not V.empty():
            fatigue = V.get()
            answer -= fatigue[1]
    
    # 돌 곡괭이 배정
    for _ in range(picks[2]):
        if not V.empty():
            fatigue = V.get()
            answer -= fatigue[0]
    
    return answer
