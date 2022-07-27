from collections import deque

n, k = map(int,input().split(" "))
q = deque(range(1,n+1))
q.reverse()
flag = 0
ans = []
while q:
    flag += 1
    num = q.pop()
    if flag == k:
        flag = 0
        ans.append(num)
    else :
        q.appendleft(num)
print("<",end="")
print(*ans,sep=", ",end="")
print(">")