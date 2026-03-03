# 월말 1번 감시
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    zero = 0
    g = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 전체 0의 개수 세기
            if arr[i][j] == 0:
                zero += 1
            # 모든 술래 탐색
            if arr[i][j] == 2:
                # 4방향 탐색
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    for c in range(1, N):
                        ni, nj = i + di * c, j + dj * c
                        # 범위 벗어나면 중단
                        if not (0 <= ni < N and 0 <= nj < N):
                            break
                        # 벽 만나면 중단
                        if arr[ni][nj] == 1:
                            break
                        # 0이면 감시 표시
                        if arr[ni][nj] == 0:
                            g[ni][nj] = 1
    # 감시된 0의 개수 세기
    guard = 0
    for i in range(N):
        for j in range(N):
            if g[i][j] == 1:
                guard += 1
    safe = zero - guard

    print(f'#{tc} {safe}')