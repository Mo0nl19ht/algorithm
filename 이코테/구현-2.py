col,row=input()
dic={
    'a':0,
    'b':1,
    'c':2,
    'd':3,
    'e':4,
    'f':5,
    'g':6,
    'h':7
}
r_col=int(dic[col])
r_row=int(row)-1
dx=[2,2,-2,-2,1,-1,1,-1]
dy=[1,-1,1,-1,2,2,-2,-2]
cnt=0
for i in range(len(dx)):
    x=r_col+dx[i]
    y=r_row+dy[i]
    if x < 0 or x>7 or y<0 or y>7:
        continue
    cnt+=1
print(cnt)