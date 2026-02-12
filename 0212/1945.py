# 간단한 소인수분해
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 소수의 개수를 0으로 초기 설정
    a = b = c = d = e = 0

    while True:
    # 소수로 나눴을 때 나머지가 0면, 개수 +1
        if N % 2 == 0:
            N = N // 2
            a += 1
        elif N % 3 == 0:
            N = N // 3
            b += 1
        elif N % 5 == 0:
            N = N // 5
            c += 1
        elif N % 7 ==0:
            N = N // 7
            d += 1
        elif N % 11 == 0:
            N = N // 11
            e += 1
        else:   # 11까지 완료하면 중단
            break

    print(f'#{tc} {a} {b} {c} {d} {e}')