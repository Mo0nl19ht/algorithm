from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort()

# 조합
perm = list(combinations(arr, 7))

# 합이 100인거 출력
for p in perm:
    p = list(p)
    if sum(p) == 100:
        p.sort
        for a in p:
            print(a)
        break
