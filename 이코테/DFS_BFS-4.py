from collections import deque
n, m = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        print("방문--", x, y)
        # 연결된 4방향 돌아보기
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 공간 벗어난 곳 제외
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물있을 때
            if g[nx][ny] == 0:
                continue
            if g[nx][ny] == 1:
                print("방문", nx, ny)
                g[nx][ny] = g[x][y]+1
                # # 어차피 맨 끝에만 가면 되니까 거기 도착하면 끊어도 될듯
                # if nx == n-1 and ny == m-1:
                #     return g[nx][ny]
                q.append((nx, ny))
            else:
                print("예외", nx, ny)

    return g[n-1][m-1]


print(bfs(0, 0))
