T = int(input())    # 테스트 케이스 입력

for tc in range(1, T+1):    # input값 받음
    N = list(map(int, input().split()))

    total = 0   # 총합 초기 설정 = 0
    for num in N:   # 리스트 순회
        if num % 2 != 0:    # 조건1: 2로 나눴을 때 0이 아니라면
            total += num    # total에 그 num을 더해라

    print(f'#{tc} {total}')