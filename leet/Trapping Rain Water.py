from collections import deque
class Solution:
        
    def trap(self, height: List[int]) -> int:
        def algo(que,stk,ans):
            if len(que) <=2:
                return ans
            while que:
                q = que.popleft()
                if stk:
                    if stk[0] <= q:

                        base = stk.popleft()
                        while stk:
                            ans= ans + (base-stk.pop())
                    else:
                        
                stk.append(q)
            if stk:
                fir = stk.popleft()
                if stk: 
                    stk.appendleft(max(list(stk)))
                ans += algo(stk,deque(),0)
            
            return ans

        for idx,h in enumerate(height):
            if h>0:
                break
        que = deque(height[idx:])
        stk = deque()
        print(max(list(que)))
        ans =0
#         while que:
#             q = que.popleft()
#             if stk:
#                 if stk[0] <= q:
                    
#                     base = stk.popleft()
#                     print(base)
#                     while stk:
#                         ans= ans + (base-stk.pop())
#             stk.append(q)
        ans = algo(que,stk,ans)
        return ans