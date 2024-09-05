def solution(priorities, location):
    answer = 0
    p = priorities[location]
    priorities[location] = -1
    
    run = True
    L = False
    
    
    while(1):
        num = priorities.pop(0)
        
        if num == -1:
            L = True
            num = p
        
        for i in priorities:
            if i == -1: i = p
            if num < i:
                run = False
                break
                
        if not run:
            if L:priorities.append(-1)
            else:priorities.append(num)
            L = False
            run = True
        else:
            answer +=1
            if L:break
        
            
    return answer
