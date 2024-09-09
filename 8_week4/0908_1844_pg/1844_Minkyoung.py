def solution(maps):
    m,n = len(maps[0]), len(maps)
    visited = [[False] * m for i in range(n)]   # m열 n행
    visited[0][0] = True
    
    dx = (0, 0, 1, -1)
    dy = (1, -1, 0, 0)

    queue = [(0,0,1)]
    
    while queue:
        x, y, dist = queue.pop(0)
        for k in range(4):
            n_x = x + dx[k]
            n_y = y + dy[k]
            if 0 <= n_x < m  and 0 <= n_y < n and maps[n_y][n_x] == 1 and not visited[n_y][n_x]:
                queue.append((n_x, n_y, dist+1))
                visited[n_y][n_x] = True

                if n_x == m-1 and n_y == n-1:
                    return dist+1

    return -1