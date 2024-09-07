# def solution(priorities, location):
    #priorities 는 우선순위, 몇번째로 실행되는지 알고싶은 프로세스 location
    # answer = 0
    # queue =  [(i,p) for i,p in enumerate(priorities)]
    # print(queue)
    
    # while True :
    #     cur = queue.pop(0)
    #     if any(cur[1] < a[1] for a in queue):
    #         queue.append(cur)
    #     else :
    #         answer += 1
    #         if cur[0] == location:
    #             return answer
    
        
def solution(priorities, location):
    answer = 0 
    max_idx = priorities.index(max(priorities))
    print(max_idx)
    
    while True:
        max_val = max(priorities)
        if (priorities[max_idx] == max_val):
            priorities[max_idx] = 0
            answer+=1
            if (max_idx == location) :
                break
        max_idx+=1
        if (max_idx >= len(priorities)):
            max_idx = 0
    return answer
        
            
    