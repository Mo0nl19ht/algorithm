arr = []
n= 9
for _ in range(n):
    arr.append(int(input()))
max_num = max(arr)
print(max_num)
print(arr.index(max_num)+1)

# 이진탐색연습
from bisect import bisect
arr = []
n= 9
for _ in range(n):
    arr.append(int(input()))
max_num = max(arr)
print(arr)
arr.sort()
print(arr)
print(bisect(arr,3))

