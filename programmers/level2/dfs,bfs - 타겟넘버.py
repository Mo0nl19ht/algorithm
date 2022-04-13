from collections import deque
# bfs
# def solution(numbers, target):
#     answer = 0
#     q = deque()
#     lenth=len(numbers)
#     q.append((numbers[0],0))
#     q.append((-numbers[0],0))
#     while q:
#         value,idx=q.popleft()
#         idx+=1
#         if idx<lenth:
#             q.append((value+numbers[idx],idx))
#             q.append((value-numbers[idx],idx))
#         else:
#             if value==target:
#                 answer+=1
#     return answer

# dfs


def solution(numbers, target):
    ans = 0
    n = len(numbers)

    def dfs(result, idx):
        if idx == n:
            if result == target:
                nonlocal ans
                ans += 1
            return
        else:
            dfs(result+numbers[idx], idx+1)
            dfs(result-numbers[idx], idx+1)
    dfs(0, 0)
    return ans
