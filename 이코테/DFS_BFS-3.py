n, m = map(int, input().split())
g = [list(map(int, input())) for _ in range(n)]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if g[x][y] == 0:
        g[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


cnt = 0
for i in range(n):
    for k in range(m):
        if dfs(i, k) == True:
            print(i, k)
            cnt += 1

print(cnt)
