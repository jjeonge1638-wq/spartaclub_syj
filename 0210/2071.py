T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input().split()))

    total = 0   # 원소들 총합 초기 설정
    cnt = 0     # 원소의 개수

    for num in N:   # 리스트 순회
        total += num    # 순회하면서 total에는 num을 더하고
        cnt += 1        # cnt에는 1을 더함

    result = round(total / cnt)    # 소수점 정리

    print(f'#{tc} {result}')
