# 최빈수 구하기
T = int(input())

for tc in range(1, T + 1):

    tc = int(input())
    sc = list(map(int, input().split()))
    # 카운트 정렬 사용
    counts = [0] * 1001   # 학생수의 최대가 1000명, 1000개의 0 리스트

    for s in sc:    # 점수 리스트 순회
        counts[s] += 1  # 카운트 리스트에서 인덱스 s에 카운트, 각 점수별 개수 세기

    maxcnt = 0  # 최빈수 초기 설정 0
    value = 0   # 최빈인 점수 원소 초기 설정 0

    for i in range(len(counts)):   # 카운트 리스트 순회
        if maxcnt < counts[i]:  # 최빈값  찾기
            maxcnt = counts[i]
            value = i           # 최빈값의 점수는 i
        elif maxcnt == counts[i] and value < i: # 최빈값이 여러개일 때
            value = i       # 최빈값의 점수 원소가 더 큰 값이 최빈값이 됨

    print(f'#{tc} {value}')