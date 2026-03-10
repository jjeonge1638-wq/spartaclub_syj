# 스위치 켜고 끄기
N = int(input())
sw = list(map(int, input().split()))

M = int(input())
st = [list(map(int, input().split())) for _ in range(M)]

# 남학생 뒤집기
for n in range(M):
    if st[n][0] == 1:
        num = st[n][1]
        for i in range(num-1, N, num):
            sw[i] = 1 - sw[i]

# 여학생 뒤집기
    else:
        num = st[n][1]

        center = num - 1
        sw[center] = 1 - sw[center]

        left = center -1
        right = center +1

        while left >= 0 and right < N and sw[left] == sw[right]:
            sw[left] = 1 - sw[left]
            sw[right] = 1 - sw[right]

            left -= 1
            right += 1

for i in range(0, N, 20):
    print(*sw[i:i+20])


