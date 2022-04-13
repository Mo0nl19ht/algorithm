def solution(nums):
    n = len(nums)//2
    arr = set(nums)
    lenth = len(arr)
    if lenth > n:
        return n
    return lenth
