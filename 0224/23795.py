# 우주 괴물
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    beam_cnt = 1    # 빔의 영향을 받는 칸 개수. 괴물 포함. 1로 시작
    wall = 0    # 벽 개수 세기 초기 값

    for i in range(N):  # 행 순회
        for j in range(N):  # 열 순회
            if arr[i][j] == 1:  # 벽 개수 세기. 1이면
                wall += 1   # +1
            if arr[i][j] == 2:  # 괴물 찾기. 2이면
                mi, mj = i, j   # 변수 지정
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  # mi, mj의 상하좌우 탐색
                    for c in range(1, N):   # 상하좌우를 탐색할 개수
                        bi, bj = mi+di*c, mj+dj*c   # 상하좌우 칸 변수를 bi, bj로 지정
                        if 0 <= bi < N and 0 <= bj < N: # 가능한 구간 지정
                            if arr[bi][bj] == 0:    # 상하좌우 칸을 순회. 값이 0이면
                                beam_cnt += 1   # beam칸 +1
                            elif arr[bi][bj] == 1:  # 값이 1이면
                                    break           # 중단
    safe = (N*N) - (wall + beam_cnt)    # 안전지댜 = 전체 - 벽 - 빔의 개수

    print(f'#{tc} {safe}')