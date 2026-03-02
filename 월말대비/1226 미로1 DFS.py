T = 10

for tc in range(1, T+1):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    si, sj = 1, 1

    def dfs(si, sj):
        visited = [[0] * 16 for _ in range(16)]
        stack = []

        visited[si][sj] = 1
        i, j = si, sj

        while True:
            if maze[i][j] == 3:
                return 1
            for di, dj in [[0,1], [1,0], [0,-1],[-1,0]]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < 16 and 0 <= nj < 16 and not visited[ni][nj] and maze[ni][nj] != 1:
                        visited[ni][nj] = 1
                        stack.append((i,j))
                        i, j = ni, nj
                        break
            else:
                if stack:
                    i, j = stack.pop()
                else:
                    break
        return 0

    print(f'#{tc} {dfs(si, sj)}')