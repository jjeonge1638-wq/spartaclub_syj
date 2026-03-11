# 병합 정렬
T = int(input())
# 병합 정렬 함수 (start ~ end)
def merge_sort(start, end):
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수 세기
    global cnt
    # 종료 조건: 원소가 하나 남았을 때, 더 이상 분할이 불가능
    if start == end - 1:
        # 정렬된 범위 리턴
        return start, end
    # 재귀호출: 두 파트로 나누고 합칠 때 정렬, 나누는 기준은 가운데
    mid = (start + end) // 2
    # 왼쪽 부분 다시 분할 후 정렬
    left_s, left_e = merge_sort(start, mid)
    # 오른쪽 부분 다시 분할 후 정렬
    right_s, right_e = merge_sort(mid, end)
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 클 때
    if arr[left_e - 1] > arr[right_e - 1]:
        cnt += 1    # cnt +1
    # 합치기
    merge(left_s, left_e, right_s, right_e)
    # 정렬된 범위 리턴
    return start, end
# 주어진 왼쪽 부분과 오른쪽 부분을 합치는 함수
def merge(left_s, left_e, right_s, right_e):
    # 왼쪽에 가장 작은 원소가 있는 인덱스
    l = left_s
    # 오른쪽에 가장 작은 원소가 있는 인덱스
    r = right_s
    # 왼쪽과 오른쪽을 합친 결과의 길이 N
    N = right_e - left_s
    result = [0] * N
    # result 배열에 들어갈 원소의 다음 자리(작은 순서)
    idx = 0
    # 병합 시작. 왼쪽 최소값 & 오늘쪽 최소값 비교. 둘 중에 작은 거 선택해서 result 의 idx 위치에 넣기
    while l < left_e and r < right_e:
        if arr[l] < arr[r]:
            result[idx] = arr[l]
            l += 1
        else:
            result[idx] = arr[r]
            r += 1
        idx += 1
    # 둘 중 한 파트에만 원소가 남아있는 경우, 남은 원소 추가
    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1

    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1
    #  result 안에는 left_s 에서 right_s 까지의 원소들이 오름차순으로 정렬. 원본 arr 에 반영
    for i in range(N):
        arr[left_s + i] = result[i]

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    merge_sort(0, N)

    print(f'#{tc} {arr[N//2]} {cnt}')