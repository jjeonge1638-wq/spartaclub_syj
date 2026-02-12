# 새로운 불면증 치료법
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    s = set()   # 0-9 담을 빈 집합
    k = 0       # N에 곱할 값

    while True:
        k += 1  # k는 1씩 증가
        sheep = N * k   # 양 개수 N*K

        for i in str(sheep):  # 양 개수를 문자열로 받아, 하나씩 순회
            s.add(i)    # 분리한 숫자를 set에 담음

        if len(s) == 10:    # 집합의 길이가 10이 되면
            break           # break

    print(f'#{tc} {N*k}')