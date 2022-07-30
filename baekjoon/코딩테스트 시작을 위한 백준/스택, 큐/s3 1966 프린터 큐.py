from collections import deque

l = int(input())

for _ in range(l):
    n, target = map(int,(input().split()))
    arr = list(map(int, input().split()))
    arr = [ (idx,i)  for idx, i in enumerate(arr)]
    que = deque(arr)
    cnt=0

    while que:
        flg=0
        p = que.popleft()
        for q in que:
            if q[1]>p[1] :
                que.append(p)
                flg=1
                break
        if flg==0:
            cnt+=1
            if target == p[0]:
                print(cnt)
                break
