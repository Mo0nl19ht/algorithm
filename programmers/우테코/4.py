def solution(s):

    i = 0
    tmp = []
    while i < len(s):
        tar = s[i]
        k = i+1
        while k < len(s) and tar == s[k]:
            k += 1

        tmp.append(k-i)
        i = k
    if s[0] == s[-1]:
        tmp[0] = tmp[0]+tmp[-1]
        del tmp[-1]
    tmp.sort()
    return tmp
