from collections import deque
def solution(queue1, queue2):
    answer = 0

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    a = sum(queue1)
    b = sum(queue2)

    while(a != b):
        if a > b:
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
        if answer >= 300000:
            answer -1
            break

    if a == b:
        return answer
    else:
        return -1