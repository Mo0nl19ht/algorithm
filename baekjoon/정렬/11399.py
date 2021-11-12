from itertools import permutations

n = int(input())
people = range(1, n+1)
time = list(map(int, input().split()))
# 사람과 소요시간을 딕셔너리로 관리
peo_time = {i: v for i, v in enumerate(time)}
peo_time_sorted = sorted(peo_time.items(), key=lambda x: x[1])

# cost는 이전 cost를 포함하므로  계속 새로운 시간소요를 더해준다
# 전체 시간 소요는 all_cost로 관리
cost = 0
all_cost = 0
for peo, time in (peo_time_sorted):
    if cost == 0:
        cost = (time)
    else:
        cost = cost+time
    all_cost += cost

print(all_cost)
