n, m = map(int, input().split())
x, y, head = map(int, input().split())


cnt = 1
chk = [[0 for k in range(m)] for i in range(n)]
head_cnt=0
go = [(-1, 0), (0, 1), (1, 0), (0, -1)]
travel = [list(map(int, input().split())) for i in range(n)]
chk[x][y] = 1
while True:
    head -= 1
    print(x, y,head,head_cnt)
    if chk[x+go[head][0]][y+go[head][1]] == 0 and travel[x+go[head][0]][y+go[head][1]]==0:
        x+=go[head][0]
        y+=go[head][1]
        chk[x][y]=1
        cnt+=1
        head_cnt=0
        if (head < 0):
            head = 3
        continue
    else:
        if (head < 0):
            head = 3
        head_cnt+=1
    if head_cnt==4:
        head+=1
        x-=go[head][0]
        y-=go[head][1]
        if travel[x][y]==1:
            break
        cnt+=1
        head_cnt=0
print(cnt)