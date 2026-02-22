# 돌 뒤집기 게임 2
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N = 돌 개수, M = 뒤집기 횟수
    stones = list(map(int, input().split()))
    for _ in range(M): # 뒤집기 M번
        # i = 센터 돌 , j = 센터 좌우로 확인할 거리
        i, j = map(int, input().split())
        # index로 접근 할 것. center = i - 1
        center = i-1
        # s는 중심에서 떨어진 거리, 1 ~ j 까지 확인
        for s in range(1, j+1):
            left = center - s # 중심 기준 왼쪽 위치
            right = center + s # 중심 기준 오른쪽 위치
            # 범위를 벗어나면 중지
            if left < 0 or right >= N:
                break
            # 조건: 양쪽 색이 같으면
            if stones[left] == stones[right]:
                # 왼쪽 오른쪽 돌 색 반전 0 -> 1 / 1 -> 0
                stones[left] = 1 - stones[left]
                stones[right] = 1 - stones[right]

    print(f'#{tc}', *stones)