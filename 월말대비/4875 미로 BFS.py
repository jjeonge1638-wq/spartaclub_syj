# 미로 queue
from collections import deque

def find_start():
    si, sj = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
    return si, sj

def bfs(si, sj):
    q = deque()
    visited = [[0] * N for _ in range(N)]

    visited[si][sj] = 1
    q.append((si,sj))

    while q:
        i, j = q.popleft()

        if maze[i][j] == 3:
            return 1

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:
                visited[ni][nj] = 1
                q.append((ni, nj))
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    si, sj = find_start()

    print(f'#{tc} {bfs(si, sj)}')