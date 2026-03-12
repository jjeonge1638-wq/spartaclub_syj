# 병합정렬
def merge_sort(start, end):
    if start == end - 1:
        return start, end

    mid = (start + end) // 2

    left_s, left_e = merge_sort(start, mid)
    right_s, right_e = merge_sort(mid, end)

    merge(left_s, left_e, right_s, right_e)

    return start, end


# 병합
def merge(left_s, left_e, right_s, right_e):
    global cnt

    l = left_s
    r = right_s

    N = right_e - left_s
    result = [0] * N

    idx = 0

    while l < left_e and r < right_e:

        if arr[l] <= arr[r]:
            result[idx] = arr[l]
            l += 1
            idx += 1

        else:
            result[idx] = arr[r]
            cnt += left_e - l
            r += 1
            idx += 1

    while r < right_e:
        result[idx] = arr[r]
        r += 1
        idx += 1

    while l < left_e:
        result[idx] = arr[l]
        l += 1
        idx += 1

    for i in range(N):
        arr[left_s + i] = result[i]


T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    wires = []

    for _ in range(N):
        A, B = map(int, input().split())
        wires.append((A, B))

    wires.sort()

    arr = [b for a, b in wires]

    cnt = 0

    merge_sort(0, N)

    print(f"#{tc} {cnt}")