from collections import deque

def solution(maps):
    answer = 0
    h = len(maps)  # 세로길이
    w = len(maps[0])  # 가로길이

    maps[h-1][w-1] = -1  # 도착지점 표시
    maps[0][0] = 2  # 1로 구분해야 하므로, 2로 시작하고 나중에 1 뺄 것임.
    
    q = deque([(0, 0)])
    
    h_add = [-1, 1, 0, 0]  # 위 아래 왼쪽 오른쪽
    w_add = [0, 0, -1, 1]
    
    while q:
        now_h, now_w = q.popleft()
        
        for i in range(4):  
            next_h = now_h + h_add[i]
            next_w = now_w + w_add[i]
            
            if next_h < 0 or next_h >= h or next_w < 0 or next_w >= w:  
                continue
            
            if next_h == h - 1 and next_w == w - 1:
                return maps[now_h][now_w] 
            
            if maps[next_h][next_w] == 1:
                # 큐에 넣고
                q.append((next_h, next_w))
                # 맵 업데이트
                maps[next_h][next_w] = maps[now_h][now_w] + 1
    
    return -1
