# 우주선 착륙 2
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0  #총 후보지 수 카운트 초기값 0

    for i in range(N):      # 델타 탐색
        for j in range(M):

            cnt = 0  # 찍을 수 있는 방향 개수 탐색
            # 총 8방향 탐색: 상, 하, 좌, 우, 대각 위, 대각 아래, 반대 대각 위, 반대 대각 아래
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,-1],[-1,1]]:
                hi, hj = i+di, j+dj     # 8방향 변수 지정
                if 0 <= hi < N and 0 <= hj < M:     # 방향 탐색 불가한 위치 제거
                    if arr[hi][hj] < arr[i][j]:     # 착륙지보다 낮으면
                        cnt += 1    # 찍을 수 있는 방향 개수 카운트
            if cnt >= 4:    # 찍을 수 있는 방향이 4개 이상이면
                result += 1 # 후보지 개수 카운트

    print(f'#{tc} {result}')
