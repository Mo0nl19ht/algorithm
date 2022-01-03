n, m = map(int, input().split())
x, y, head = map(int, input().split())
x -= 1
y -= 1

cnt = 0
chk = [[0 for k in range(m)] for i in range(n)]
d_ck = 0
go = [(0, 1), (1, 0), (0, -1), (-1, 0)]
travel = [list(map(int, input().split())) for i in range(n)]
chk[x][y] = 1
while True:
    head -= 1
    print(x, y)

    if chk[x+go[head][0]][y+go[head][1]] == 1:
        d_ck += 1
        if (head < 0):
            head = 3
        continue
    x += go[head][0]
    y += go[head][1]
    chk[x][y] = 1
    cnt += 1
    if (head < 0):
        head = 3

print(cnt)


# travel[x+go[0][0]][y+go[0][1]] == 1 and
#             travel[x+go[1][0]][y+go[1][1]] == 1 and
#             travel[x+go[2][0]][y+go[2][1]] == 1 and
#             travel[x+go[3][0]][y+go[3][1]] == 1
