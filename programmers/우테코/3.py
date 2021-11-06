def solution(ings, menu, sell):
    mm = []
    ii = []
    ss = []
    dic = {}
    for m in menu:
        mm.append(m.split())
    for i in ings:
        ii.append(i.split())
    ii = dict(ii)
    for s in sell:
        ss.append(s.split())
    for m in mm:
        sum = 0
        for i in m[1]:
            sum += int(ii[i])
        dic[m[0]] = int(m[2])-sum
    result = 0
    for s in ss:
        result += dic[s[0]] * int(s[1])
    return result
