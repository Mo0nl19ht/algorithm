n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
# sorted_a = sorted(a)
# sorted_b = sorted(b, reverse=True)
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
print(sum(a))
