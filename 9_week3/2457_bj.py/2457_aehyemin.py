from collections import deque
def solution(queue1, queue2):
    #큐는 선입선출
    #합을 같게 만들어야함
    #큰 큐에서 먼저 꺼낸다음에 작은 큐에 넣고 검사
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    sumq1 = sum(q1)
    sumq2 = sum(q2)
    total_sum = sumq1 + sumq2
    goal = (total_sum)//2
    limit = 3*(len(q1)+len(q2))
    
    if total_sum%2 != 0 :
        return -1
    #테스트 1번 케이스 실패, 다른 케이스 시간초과
    while cnt < limit:
        if sumq1 == sumq2 :
            return cnt
        
        elif sumq1 > goal:
            poping = q1.popleft()
            sumq1 -= poping
            
            q2.append(poping)
            sumq2 += poping
            
        else:
            poping = q2.popleft()
            sumq2 -= poping
            
            q1.append(poping)
            sumq1 += poping
        cnt += 1
    return -1



# from collections import deque
# def solution(queue1, queue2):
#     #큐는 선입선출
#     #합을 같게 만들어야함
#     #큰 큐에서 먼저 꺼낸다음에 작은 큐에 넣고 검사
#     q1 = deque(queue1)
#     q2 = deque(queue2)
#     goal = (sum(queue1)+sum(queue2))//2
#     cnt = 0
#     while sum(q1) != sum(q2):
#         if sum(q1) > sum(q2):
#             poping = q1.popleft()
#             #print(poping)
#             q2.append(poping)
#             cnt += 1
#         else : # sum(q1) < sum(q2):
#             poping = q2.popleft()
#             #print(poping)
#             q1.append(poping)
#             cnt += 1
#         if cnt > len(q1) + len(q2):
#             return -1
#     return cnt
