def solution(priorities, location):
    answer = 0
    
    while priorities:
        head = priorities.pop(0)

        # priorities 중 head 보다 큰게 하나라도 있으면
        if any(head < p for p in priorities):
            priorities.append(head)
            if location == 0:
                location = len(priorities) - 1 # 큐의 맨 뒤로 보내니까 location도 그에 맞게
            else:
                location -= 1 # 프로레스 하나가 실행되어 큐 크기가 줄었으니 location도 맞춰줌
        else: # 큰게 없으면 
            answer += 1 # 프로세스 한개 실행했으니 실행횟수 + 1 해줌
            if location == 0: # 원하는 프로세스가 실행된 경우
                return answer
            location -= 1
