# 증가하는 사탕 수열
T = int(input())
# C를 기준으로 B 줄임, B를 기준으로 A 줄임
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    eaten = 0   # 먹은 수 계산
    # B 조정: 최소값이니깐 C-1까지 줄여야 함
    if B >= C:
        eaten += B-(C-1)
        B = C - 1
    # A 조정: B-1까지 줄임
    if A >= B:
        eaten += A-(B-1)
        A = B-1
    # 불가능 조건: A,B가 0이하
    if A < 1 or B < 1:
        ans = -1
    else:
        ans = eaten

    print(f'#{tc} {ans}')