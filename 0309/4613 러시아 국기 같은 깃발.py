# 러시아 국기 같은 깃발
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    # 각 행을 어떤 색으로 만들 때 필요한 횟수 저장
    rowW = [0] * N  # i행을 W로 바꿀 횟수 저장
    rowB = [0] * N  # i행을 B로 바꿀 횟수 저장
    rowR = [0] * N  # i행을 R로 바꿀 횟수 저장

    for i in range(N):  # 모든 행 순회
        for c in flag[i]:  # 각 행의 모든 문자 순회
            if c != 'W':
                rowW[i] += 1
            if c != 'B':
                rowB[i] += 1
            if c != 'R':
                rowR[i] += 1
    # 큰 값으로 최소값 설정
    min_v = 10 ** 9
    # 구간 정하기
    for endW in range(N - 2):  # 흰색 구간 : 최소 2개 행은 남겨야 함
        for endB in range(endW + 1, N - 1):  # 파란 구간: 최소 1개 행은 남겨야 함
            # 빨간 구간은 자동 설정
            cnt = 0  # 구역 분할에서 필요한 횟수
            # W 구간 횟수
            for i in range(0, endW + 1):
                cnt += rowW[i]
            # B 구간 횟수
            for i in range(endW + 1, endB + 1):
                cnt += rowB[i]
            # R 구간 횟수
            for i in range(endB + 1, N):
                cnt += rowR[i]
            # 최소값 갱신
            min_v = min(min_v, cnt)

    print(f'#{tc} {min_v}')



