# 돌 뒤집기 게임 1
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 돌 개수, M: 뒤집기 횟수
    stones = list(map(int, input().split()))
    for _ in range(M): # 뒤집기 M번
        # i = 시작 돌, j = 뒤집을 돌 개수
        i, j = map(int, input().split())

        color = stones[i-1] # i 돌색으로 변경, 인덱스로 접근. i-1
        # 구간설정 i ~ (i + j -2)
        # i + j-1이 마지막 인덱스를 넘는 경우 고려. i+j와 N의 최소값
        for s in range(i-1, min(i-1+j,N)):
            stones[s] = color # 구간 안의 돌을 첫 번째 돌 색으로 변경

    print(f'#{tc}', *stones)