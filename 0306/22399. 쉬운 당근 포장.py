# 쉬운 당근 포장
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ci = list(map(int, input().split()))

    ci.sort()
    minv = 10 ** 9

    for i in range(N - 2):
        if ci[i] == ci[i + 1]:
            continue
        for j in range(i + 1, N - 1):
            if ci[j] == ci[j + 1]:
                continue

            s = i + 1
            m = j - i
            l = N - j - 1

            diff = max(s, m, l) - min(s, m, l)
            minv = min(minv, diff)
    if minv == 10 ** 9:
        minv = -1

    print(f'#{tc} {minv}')