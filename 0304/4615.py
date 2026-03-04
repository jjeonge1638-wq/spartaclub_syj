# 오셀로 게임
T = int(input())

di = [-1,1,0,0] + [-1,-1,1,1]
dj = [0,0,-1,1] + [-1, 1,1,-1]

for tc in range(1, T+1):
    N, M = map(int, input().split())
        # 초기 보드 상태
    board = [[0] * N for _ in range(N)]

    board[N//2-1][N//2-1] = board[N//2][N//2] = 2
    board[N//2][N//2-1] = board[N//2-1][N//2] = 1

    for _ in range(M):
        i, j, c = map(int, input().split())
        # 문제에서 행번호, 열번호 1씩 시작
        i -= 1
        j -= 1
        board[i][j] = c
    # (i,j) 위치에 돌을 놓았으면 오셀로 게임 규칙에 따라서 게임을 진행
    # 8방향을 탐색하면서 돌이 있나 확인
    # 방향을 하나 정했으면 해당 방향으로 쭈우우우욱 가야 함
    # 만날 수 있는 상황 리스트
    # 1. 나랑 다른 색 돌을 만남
            # 마지막에 나랑 같은 색 돌을 만나면 사이에 있는 돌 모두 뒤집음
            # 내가 다른 색의 돌을 만날 때마다 이 돌은 나중에 뒤집을 수도 있으니 위치를 저장 해놔야 함
    # 2. 배열 범위 벗어남. 반복 중단, 다음 방향
    # 3. 돌이 없는 곳을 만남. 반복 중단, 다음 방향
        for d in range(8):
            # 뒤집을 돌 위치를 기억할 lst
            reverse_lst = []
            for k in range(1, N):
                ni = i + di[d] * k
                nj = j + dj[d] * k
                if not (0 <= ni < N and 0 <= nj < N):
                    break

                elif board[ni][nj] == 0:
                    break

                elif board[ni][nj] != c:
                    reverse_lst.append((ni, nj))

                elif board[ni][nj] == c:
                    while reverse_lst:
                        ri, rj = reverse_lst.pop()
                        board[ri][rj] = c

                    break

    w = 0
    b = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                w += 1
            elif board[i][j] == 1:
                b += 1

    print(f'#{tc} {b} {w}')