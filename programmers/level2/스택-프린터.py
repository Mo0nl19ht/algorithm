def solution(priorities, location):
    answer = 0
    pri = [(index, val) for index, val in enumerate(priorities)]
    cnt = 0
    while pri:
        a = pri.pop(0)
        flg = 0
        for i in pri:
            if a[1] < i[1]:
                pri.append(a)
                flg = 1
                break
        if flg == 0:
            cnt += 1
            if a[0] == location:
                return cnt
        flg = 0

    return cnt
