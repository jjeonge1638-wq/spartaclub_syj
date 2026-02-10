T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:   # N과 M 중에 어떤 것이 항상 크거나 작다는 설정 X
        A, B = B, A     # 둘 다 가능하도록 맞춰 줌
        N, M = M, N     # 기본 설정은 N이 클 때, N이 작을 때는 배열을 바꿔 줌

    maxv = 0    # 최대값 기본 설정 0
    for i in range(N-M+1):      # 큰 배열에서 가능한 작은 배열의 범위
        s = 0                   # 곱의 총합 초기 설정 0
        for j in range(M):      # 작은 배열과 큰 배열에서의 작은 배열 곱의 합
            s += (A[i+j]*B[j])  # 합을 s에 더함. 작은 배열의 인덱스는 항상 같고
                                # 큰 배열의 인덱스는 j보다 i만큼 밀려서 시작
        if maxv < s:        # 모두 합한 후 maxv가 합보다 작으면
            maxv = s        # maxv = s

    print(f'#{tc} {maxv}')