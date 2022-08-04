def solution(prices):
    ans=[]
    
    for idx,p in enumerate(prices):
        cnt=0
        arr = prices[idx+1:]
        for c,a in enumerate(arr):
            if a < p:
                cnt = c+1
                break
        if cnt==0:
            cnt = len(arr)
        ans.append(cnt)
        
            
            
    return ans