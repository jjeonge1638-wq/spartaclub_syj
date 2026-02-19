# 농작물 수확하기
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    value = 0

    for i in range():
        for j in range():
# 열로 한 줄씩 순회하는 방식으로 접근
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    value = 0	# 가치 초기 설정 0
    mid = N // 2	# 열의 중앙 인덱스

    for j in range(N):	# d = 중앙과 각 열의 거리
        d = abs(mid - j)
        for i in range(d, N-d):		# 행의 범위 d, N-d-1
            value += farm[i][j]		# 순회하면서 가치 +1

    print(f'#{tc} {value}')
