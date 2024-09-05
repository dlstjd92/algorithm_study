def solution(priorities, location):
    order = sorted(priorities, reverse=True)
    pt = 0 # 프리오리티 포인터
    opt = 0 # 오더 포인터
    answer = 0
    while(1):
        if priorities[pt] == order[opt]: # 목표를 찾으면?
            opt+=1 # 다음순위
            answer+=1 # 카운터 1올리고
            if pt == location: # 만약 로케이션까지 같으면?
                break # 탈출
            priorities[pt] = None # 해당위치 비우기
        else:
            if pt >= len(priorities)-1: # 리스트 범위 넘어가면
                pt = 0 # 처음으로
            else:
                pt+=1 # 다음포인터
    return answer
