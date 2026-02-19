# 원재의 메모리 복구하기
T = int(input())

for tc in range(1,T+1):
    # 굳이 리스트 필요없음, strip()으로 공백, 줄바꿈 제거
    m = input().strip()

    cnt = 0 # 변화 개수 초기 값
    first = '0' # 초기화 값

    for b in m: # 문자열 m 순회
        if b != first:  # bit가 초기화 값과 다르면
            cnt += 1    # 변화 개수 증가
            first = b   # 초기화 값을 b로 변경

    print(f'#{tc} {cnt}')