# 미로 2 queue
from collections import deque

def bfs(si, sj):
    q = deque()
    visited = [[0] * 100 for _ in range(100)]

    visited[si][sj] = 1
    q.append((si, sj))

    while q:
        i, j = q.popleft()

        if maze[i][j] == 3:
            return 1

        for di, dj in[[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < 100 and 0 <= nj < 100 and not visited[ni][nj] and maze[ni][nj] != 1:
                visited[ni][nj] = 1
                q.append((ni, nj))
    return 0

T = 10
for tc in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]

    si, sj = 1, 1

    print(f'#{tc} {bfs(si,sj)}')