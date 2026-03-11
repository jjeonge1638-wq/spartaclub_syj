# 퀵 정렬
T = int(input())
# A 정렬할 배열
# l, r 정렬 배열의 시작 인덱스, 종료 인덱스
def quick_sort(A, l, r):
    if l < r:
        p = hoare_partition(A, l, r)
        quick_sort(A, l, p - 1)
        quick_sort(A, p + 1, r)

def hoare_partition(A, l, r):
    p = A[l]
    i = l
    j = r

    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(A, 0, N - 1)
    print(f'#{tc} {A[N//2]}')