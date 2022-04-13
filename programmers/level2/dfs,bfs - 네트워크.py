from collections import deque


def dfs(computers, visited, idx, n):
    visited[idx] = True
    for i in range(n):
        if i != idx and visited[i] == False and computers[idx][i] == 1:
            dfs(computers, visited, i, n)
    return


def bfs(computers, visited, idx, n):
    visited[idx] = True
    q = deque()
    q.append(idx)
    while q:
        com = q.pop()
        for i in range(n):
            if com != i and visited[i] == False and computers[com][i] == 1:
                visited[i] = True
                q.append(i)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if visited[i] == False:
            answer += 1
            bfs(computers, visited, i, n)
    return answer
