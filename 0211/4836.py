# 색칠하기
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 0인 10*10 배열 만들기
    board = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):   # 행 순회
            for j in range(c1, c2+1): # 열 순회
                board[i][j] += color    # 0인 칸에 빨강은 1, 파랑은 2를 더함
    # 보라색(빨1+파2=3) 세기
    p = 0   # 보라색 초기값 0
    for i in range(10):    # 행 순회
        for j in range(10): # 열 순회
            if board[i][j] == 3:  # 칸의 값이 3이면
                p +=1   # 보라색 개수 +1

    print(f'#{tc} {p}')

