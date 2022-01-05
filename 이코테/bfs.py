from collections import deque

def bfs(g,start,visit):
    q=deque([start])
    visit[start]=True
    while q:
        v=q.popleft()
        print(v,end=' ')
        for i in g[v]:
            if not visit[i]:
                q.append(i)
                visit[i]=True

g = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visit = [False]*9

bfs(g,1,visit)