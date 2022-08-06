def dfs(start,link,visited):
    if visited[start]==1:
        return
    visited[start] = 1
    for idx,a in enumerate(link[start]):
        if a==1 and visited[idx]==0:
            dfs(idx,link,visited)
    return
n= int(input())
m = int(input())
link = [[0 for _ in range(n+1)]for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    link[a][b] = 1
    link[b][a] = 1

dfs(1,link,visited)
print(visited.count(1)-1)