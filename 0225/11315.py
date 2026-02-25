# 오목 판정
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    stone = [list(input()) for _ in range(N)] 
    # 답을 No로 정해두고 탐색
    answer = 'NO'
    # 델타 탐색(전체 칸)
    for i in range(N):
        for j in range(N):
            # 돌이 o인 경우만 가로.세로.대각선 탐색
            if stone[i][j] == "o":
                # 4방향 탐색: 가로, 세로, 대각\, 반대 대각/  탐색 
                for di, dj in [[0,1],[1,0],[1,1],[1,-1]]:
                    cnt = 1   # 돌 개수 세기. 초기 값 0
                    for c in range(1,5):    # 4방향 탐색 구간 기준 돌 포함 5개니깐 1~4
                        ni, nj = i+di*c, j+dj*c
                        if 0 <= ni < N and 0 <= nj < N: # 4방향 탐색 불가능한 곳 제외
                            if stone[ni][nj] == "o":    # 돌이 o이면
                                cnt += 1                # cnt +1
                            else:                       # 아니면
                                break                   # 중단
                    if cnt >= 5:        # cnt가 5보다 크거나 작다면
                        answer = "YES"  # 대답을 YES로 변경
    print(f'#{tc} {answer}')    