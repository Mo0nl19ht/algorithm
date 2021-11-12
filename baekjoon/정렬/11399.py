from itertools import permutations

n = int(input())
people = range(1, n+1)
time = list(map(int, input().split()))

peo_time = {i: v for i, v in enumerate(time)}
peo_time_sorted = sorted(peo_time.items(), key=lambda x: x[1])


cost = 0
all_cost = 0
for peo, time in (peo_time_sorted):
    if cost == 0:
        cost = (time)
    else:
        cost = cost+time
    all_cost += cost

print(all_cost)
