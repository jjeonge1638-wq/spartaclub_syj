# 상호의 배틀 필드
T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    field = [list(input()) for _ in range(H)]

    N = int(input())
    commands = input()

    # 방향 설정
    dirs = {'^':0, 'v':1, '<':2, '>':3}
    delta = [(-1,0), (1,0), (0,-1), (0,1)]
    tank = ['^','v','<','>']

    # 전차 찾기
    for i in range(H):
        for j in range(W):
            if field[i][j] in dirs:
                ti, tj = i, j
                d = dirs[field[i][j]]
    for c in commands:
        if c in "UDLR": # 방향 이동
            if c == 'U': d = 0
            elif c == 'D': d = 1
            elif c == 'L': d = 2
            elif c == 'R': d = 3

            field[ti][tj] = tank[d]

            ni = ti + delta[d][0]
            nj = tj + delta[d][1]

            if 0 <= ni < H and 0 <= nj < W:
                if field[ni][nj] == '.':
                    field[ti][tj] = '.'
                    ti, tj = ni, nj
                    field[ti][tj] = tank_dir_symbol[d]

        # 포탄 발사?
            # 이 부분 구현을 어떻게 해야 할지 모르겠습니다......
    # 출력
    print(f"#{tc}", end=" ")
