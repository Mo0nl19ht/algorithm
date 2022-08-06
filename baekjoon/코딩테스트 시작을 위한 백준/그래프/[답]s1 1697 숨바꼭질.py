from collections import deque
# def trip(x,target,t,max_t):
#     if x < 0 or x>100000:
#         return -1
#     if t>max_t:
#         return max_t
#     if x == target:
#         return t
#     t+=1
#     c=trip(2*x,target,t,max_t)
#     a=trip(x+1,target,t,max_t)
#     b=trip(x-1,target,t,max_t)
    
#     arr = [a,b,c]
#     min = max_t
    
#     for tt in arr:
#         if tt>0 and min >tt:
#             min=tt
#     return min
  #시간초과남

n ,k= map(int,input().split())
max_t=abs(k-n)
max_num = 100000
t_list = [0 for _ in range(max_num+1)]

q = deque()
q.append(n)
while q:
    x = q.popleft()
    if x==k:
        print(t_list[x])
        break
    for a in (x+1,x-1,x*2):
        if 0<=a<=max_num and t_list[a]==0:
            t_list[a] = t_list[x]+1
            q.append(a)


