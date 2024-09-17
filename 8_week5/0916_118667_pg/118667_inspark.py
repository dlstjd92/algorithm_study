import copy
from collections import deque

def solution(queue1, queue2):
    
    # 대놓고 그리디네?
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    first1 = copy.deepcopy(queue1)
    # first2 - queue2
    
    answer = 0
    
    if max(queue1 + queue2) > sum(queue1 + queue2)/2 or sum(queue1 + queue2)%2 != 0:
        return -1

    a = sum(queue1)
    b = sum(queue2)

    while(a != b):
        if a > b:
            temp = queue1.popleft()
            a-=temp
            b+=temp
            queue2.append(temp)
        else:
            temp = queue2.popleft()
            a+=temp
            b-=temp
            queue1.append(temp)
        answer += 1
        
        if first1 == queue1 or answer >= 600000:
            answer = -1
            break

    return answer
