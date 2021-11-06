def solution(arr):
    ans = []
    a1 = arr.count(1)
    a2 = arr.count(2)
    a3 = arr.count(3)
    ma = [a1, a2, a3]
    idx = (max(ma))

    ma = idx
    ans.append(ma-a1)
    ans.append(ma-a2)
    ans.append(ma-a3)

    return ans
