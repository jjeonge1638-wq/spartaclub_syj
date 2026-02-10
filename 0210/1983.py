T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    std = [list(map(int, input().split())) for _ in range(N)]

    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    rank = []   # 총점으로 매긴 성적 순위 담을 빈 리스트
    for s in std:   # 학생별 중, 기, 과 2차원 배열 순회
        # 2차원 배열 속 각 리스트의 index 0, 1, 2 자리 성적 비율 반영 후 모두 합. total에 할당
        total = (s[0] * 0.35) + (s[1] * 0.45) + (s[2] * 0.2)
        rank.append(total)  # total값을 rank 리스트에 저장

    target = rank[K-1]  # k번째 학생의 점수 저장. 내림차순으로 정리하면 순서가 바뀌니깐 정렬 전 미리 저장
    rank.sort(reverse = True)   # rank 리스트를 내림차순으로 정렬

    # 정렬된 rank리스트 속 K의 인덱스 위치 찾기
    idx = 0     # 초기 인덱스 설정 0
    for i in range(N):  # rank 리스트 순회
        if rank[i] == target:   # rank[i]중 target 점수와 같다면
            idx = i             # i는 K이의 rank 인덱스 위치
            break               # 인덱스 위치 찾았스니깐 종료

    M = N // 10     # M은 한 학점당 가능한 학생 수
    print(f'#{tc} {grade[idx//M]}') # M명씩 학점이 바뀜. 순위를 학점 인덱스 번호로
