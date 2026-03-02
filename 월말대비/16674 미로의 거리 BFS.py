# 미로의 거리 Queue
from collections import deque
# bfs에서 사용할 큐 자료구조 불러옴

T = int(input())
# 시작 점 찾는 함수
def find_start():
    si, sj = 0, 0   # 시작점 초기 값 설정
    for i in range(N): # 행 우선 순회
        for j in range(N):
            if maze[i][j] == 2: # 2가 시작 점
                si, sj = i, j   # 시작점 저장
    return si, sj  # 찾으면 반환
# 시작 좌표에서 출발하여 도착점까지의 최단거리 함수
def bfs(si, sj):
    q = deque() # bfs용 큐 생성
    # 방문 여부, 거리 저장 배열
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1 # 시작 지점을 방문으로 표시, 거리는 1부터

    q.append((si, sj))  # 시작 좌표 큐에 삽입

    while q:    # 큐가 빌 때까지 반복
        i, j = q.popleft()  # 가장 먼저 들어온 좌표 꺼내기

        if maze[i][j] == 3: # 도착점에 도달. 현위치 3이면
            return visited[i][j] - 2    # 시작, 방문 제외(-2) 이동 거리 반환
        # 4방향 탐색
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            # 조건 3개: 델타 범위 안, 방문 X, 벽 X
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and maze[ni][nj] != 1:
                visited[ni][nj] = visited[i][j] + 1 # 현재 위치 거리 +1을 다음 위치에 저장
                q.append((ni, nj))  # 다음 위치를 큐에 추가
    return 0    # 도착점에 도달하지 못하면 0반환

for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작점 좌표 찾기
    si, sj = find_start()

    print(f'#{tc} {bfs(si, sj)}')
