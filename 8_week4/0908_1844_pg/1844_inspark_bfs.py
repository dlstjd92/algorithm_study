from collections import deque

def solution(maps):
    answer = 0
    h = len(maps)
    w = len(maps[0])

    queue = deque([(0, 0, 1)])
    visit = [[0 for _ in range(w)] for _ in range(h)]
    visit[0][0] = 1

    while(queue):
        nh, nw, dis = queue.popleft()

        if nh == h - 1 and nw == w - 1:
            return dis
        
        for dh, dw in [(-1,0), (0,-1), (1,0), (0,1)]:
            temph = nh + dh
            tempw = nw + dw
            if 0 <= temph < h and 0 <= tempw < w and not visit[temph][tempw] and maps[temph][tempw] == 1:
                visit[temph][tempw] = 1
                queue.append((temph,tempw,dis+1))


    return -1

