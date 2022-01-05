n,m =map(int,input().split())
g=[ list(map(int,input())) for _ in range(n) ]
visit=[[False]*m for _ in range(n)]
def dfs(g,i,k,visit):
    visit[v]=True
    for x in range(i,len(g)):
        for y in g[x][k+1:]:




for i in range(n):
    for k in range(m):
        if g[i][k]==0 and visit[i][k]==False:
            
