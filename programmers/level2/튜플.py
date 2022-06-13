def solution(s):
    answer = []
    arr = s.split("},")
    new = []
    for a in arr:
        a = a.strip("{")
        a = a.strip("}")
        new.append((a.split(",")))
    new.sort(key=lambda x: len(x))
    for li in new:
        li = list(map(int, li))
        s = (set(li)-set(answer))
        answer.append(int(s.pop()))
    return answer
