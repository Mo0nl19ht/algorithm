ch = False

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    ch = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            ch = True
            arr[j], arr[j+1] = arr[j+1], arr[j]
    if not ch:
        print(i+1)
        break
    print(i, arr)

#버블정렬할때 정렬이 완성되는 그 index+1