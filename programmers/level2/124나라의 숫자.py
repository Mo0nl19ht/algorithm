def solution(n):
    dic = {
        0: 1,
        1: 2,
        2: 4
    }
    answer = ""
    while n > 0:
        n -= 1
        answer = answer + str(dic[n % 3])
        n = n//3

    return "".join(reversed(answer))
