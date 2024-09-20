from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1, sum2 = sum(queue1), sum(queue2)
    
    count = sum1 + sum2
    max_operations = len(queue1) + len(queue2) * 2  # 무한 루프 방지를 위해 설정
    
    while sum1 != sum2:
        if answer > max_operations:
            return -1
        
        answer += 1
        
        if sum1 < sum2:
            if len(queue2) == 1:
                return -1
            val = queue2.popleft()
            queue1.append(val)
            sum1 += val
            sum2 -= val
        else:
            if len(queue1) == 1:
                return -1
            val = queue1.popleft()
            queue2.append(val)
            sum2 += val
            sum1 -= val
    
    return answer
