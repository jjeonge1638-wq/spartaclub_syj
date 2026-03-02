# 미로1 queue
from collections import deque

T = 10

def bfs(si, sj):
    q= deque()
    visited = [[0] * 16 for _ in range(16)]
    visited[si][sj] = 1
    q.append((si, sj))

    while q:
        i, j = q.popleft()

        if maze[i][j] == 3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < 16 and 0 <= nj < 16 and not visited[ni][nj] and maze[ni][nj] != 1:
                visited[ni][nj] = 1
                q.append((ni, nj))
    return 0

for tc in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    si, sj = 1, 1

    print(f'#{tc} {bfs(si, sj)}')
