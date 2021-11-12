from itertools import permutations

n = int(input())
people = range(1, n+1)
time = list(map(int, input().split()))

perm = list(permutations(people, n))
min_cost = 0
for _, p in enumerate(perm):
    p = list(p)
    cost = 0
    all_cost = 0
    for i, v in enumerate(p):
        if i == 0:
            cost = (time[v-1])
        else:
            # tmp.append(tmp[i-1]+time[v-1])
            cost = cost+time[v-1]
        all_cost += cost
    if _ == 0:
        min_cost = all_cost
    elif min_cost > all_cost:
        min_cost = all_cost
print(min_cost)
