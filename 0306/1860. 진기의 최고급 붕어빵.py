# 진기의 최고급 붕어빵
T = int(input())

for tc in range(1, T+1):
    # 예약 손님 수, 걸리는 시간, 만들 수 있는 붕어빵 개수
    N, M, K = map(int, input().split())
    # 초 수가 순서대로 주어지지 않음
    arrive = sorted(map(int, input().split()))
    # 임시 답
    answer = "Possible"
    # 예약 손님 동안
    for i in range(N):
        bread = (arrive[i] // M) * K   # 지금까지 만든 붕어빵

        if bread < i + 1:              # 손님 수보다 적으면
            answer = "Impossible"
            break

    print(f'#{tc} {answer}')