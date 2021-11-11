n = int(input())
arr = list(map(int, (input()).split()))
# 문제에서 서로 다른 수 라고 했으므로 중복제거
sor = sorted(list(set(arr)))
# 시간복잡도 작게하기 위해 딕셔너리 변환
sor = {v: i for i, v in enumerate(sor)}
# 좌표변환
new = []
for i in arr:
    print(sor[i], end=" ")
