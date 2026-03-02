# 스택 미로
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작 지점 초기 설정
    si, sj = 0, 0
    # 2차원 배열 순회로 시작 지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2: # 2라면 시작지점
                si, sj = i, j   # 시작 지점 변수 지정

    # dfs 함수
    def dfs(si, sj):
        # 방문 기록 리스트 만들기. 0이면 방문 한 적 없음. 1이면 방문 함.
        visited = [[0] * N for _ in range(N)]
        stack = []  # 빈 스택 생성
        # 현재 방문 지점. 1부터 기록
        visited[si][sj] = 1
        i, j = si, sj

        while True:
            # 중단 조건: 현재 위치가 출구
            if maze[i][j] == 3:
                return 1    # 출구를 찾으면 답 1 반환
            # 현위치에서 4방향 탐색
            for di, dj in [[0,1], [1,0], [0,-1],[-1,0]]:
                ni, nj = i+di, j+dj
                # 조건 3개: 2차원 배열 범위 안, 방문한 적 X, 벽 X
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:
                    visited[ni][nj] = 1  # ni, nj 방문체크. 1로 표시
                    stack.append((i, j))    # 돌아 올 위치 기억
                    i, j = ni, nj   # ni, nj 이동
                    break
            else:
                # 중단이 안 됐다. 3을 못 찾음. -> 이전 방문지점으로 돌아 감
                if stack: # 스택이 안 비었다면
                    i, j = stack.pop() # 가장 최근(마지막)방문 지점 반환
                else: # 스택이 비었으면 다 가봄. 중단
                    break
        # 반복문 후에도 출구 찾지 못 하면 0반환
        return 0

    print(f'#{tc} {dfs(si, sj)}')