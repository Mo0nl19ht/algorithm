from collections import deque

n=int(input())
flg=0
for _ in range(n):
    arr = deque(input())
    stk = deque()
    while arr:
        head = (arr.popleft())
        if not stk:
            stk.append(head)
            continue
        p = stk.pop()
        if p==")" and not stk:
            flg=1
            break
        if p==head:
            stk.append(p)
            stk.append(head)
    if flg==1:
        print("NO")
        flg=0
    elif stk:
        print("NO")
    else :
        print("YES")