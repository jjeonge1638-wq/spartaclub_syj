# 경비원의 감시
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    zero = 0
    guard = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                zero += 1
            if arr[i][j] == 2:
                si, sj = i, j
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                    for c in range(1,N):
                        ni, nj = si+di*c, sj+dj*c
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] == 0:
                                guard += 1
                            elif arr[ni][nj] == 1:
                                break
    result = zero - guard

    print(f'#{tc} {result}')

