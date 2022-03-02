import math
from collections import deque


def solution(pro, spd):
    day = []
    for i in range(len(pro)):
        day.append(math.ceil((100-pro[i])/spd[i]))
    cnt = 0
    ans = []
    q = deque(day)
    while q:
        first = q.popleft()
        cnt += 1
        while q and first >= q[0]:
            q.popleft()
            cnt += 1
        ans.append(cnt)
        cnt = 0

    return ans
