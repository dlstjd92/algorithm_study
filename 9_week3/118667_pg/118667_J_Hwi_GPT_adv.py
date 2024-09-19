from collections import deque
def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    a = sum(queue1)
    b = sum(queue2)
    total = a + b
    if total % 2 != 0:
        return -1
    
    target = total // 2
    max = len(queue1) * 3

    while a != target and answer < max:
        if a > target:
            num = queue1.popleft()
            queue2.append(num)
            a -= num
            b  += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            a += num
            b -= num
        answer += 1
    if a == target:
        return answer
    else:
        return -1